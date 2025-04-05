from transformers import pipeline, set_seed
from datasets import load_from_disk
import matplotlib.pyplot as plt
import pandas as pd
from evaluate import load
metric = load("rouge")
from evaluate import load as load_metric
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
import nltk
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
import torch
import json
from textSummarizer.entity import ModelEvaluationConfig

#Creating components for Model_Evaluation:
class ModelEvaluation:

    #Defining the constructor:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config


    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            batch = list_of_elements[i : i + batch_size]
            if not batch:  # Prevents yielding empty batch
                break
            print(f"Processing batch {i // batch_size + 1}/{(len(list_of_elements) + batch_size - 1) // batch_size}")
            yield batch



    
    # Define the device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    #A function to calculate the metric of the test dataset:
    def calculate_metric_on_test_ds(self,dataset,metric,model,tokenizer,batch_size = 4,device = device,column_text = "article",column_summary = "highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text],batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size))

        for article_batch,target_batch in tqdm(
            zip(article_batches,target_batches),total = len(article_batches)):

            inputs = tokenizer(article_batch,max_length = 1024,truncation = True,padding = "max_length",return_tensors = "pt")

            summaries = model.generate(input_ids = inputs["input_ids"].to(device),
                                        attention_mask = inputs["attention_mask"].to(device),
                                        length_penalty = 0.8,num_beams = 8, max_length = 128)

            ''' parameter for length penalty ensures that the model does not generate sequences that are too long.'''

            # Finally, we decode the generated texts,
            # replace the token, and add the decoded texts with the references to the metric:
            decoded_summaries = [tokenizer.decode(s,skip_special_tokens = True,clean_up_tokenization_spaces = True) for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions = decoded_summaries,references = target_batch)

        score = metric.compute()
        return score


    #A function to evaluate metric:
    def evaluate(self):

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        #Loading data:
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1","rouge2","rougeL","rougeLsum"]
        rouge_metric = load_metric('rouge') 

        # Defining the score:
        score = self.calculate_metric_on_test_ds(
            dataset_samsum_pt['test'], rouge_metric,model_pegasus,tokenizer,
            column_text = "dialogue",column_summary = "summary"
        )

        with open("artifacts/model_evaluation/rouge_raw_scores.json", "w") as f:
            json.dump({k: float(v) for k, v in score.items()}, f, indent=4)

        #Defining the rouge dictionary for metrices:
        rouge_dict = dict((rn,score[rn]) for rn in rouge_names)

        #Converting the metric dictionary into dataframe:
        df = pd.DataFrame(rouge_dict,index = ['pegasus'])

        #Saving the dataframe in csv format:
        df.to_csv(self.config.metric_file_name,index = False)