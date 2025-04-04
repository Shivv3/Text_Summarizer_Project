from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
from textSummarizer.entity import ModelTrainerConfig
import os

class ModelTrainer:

    #Constructor:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    #A function to train the model:
    def train(self):

        # Setting up the device:
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Setting up the tokenizer:
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

        #Loading the data:
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        dataset_samsum_pt = dataset_samsum_pt.remove_columns(
            [col for col in dataset_samsum_pt["train"].column_names if col not in ["input_ids", "attention_mask", "labels"]]
        )
        dataset_samsum_pt.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])


        # Setting up the model:
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
    

        # Setting up the seq2seq2 Collator:
        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer,
            model=model_pegasus,
            label_pad_token_id=-100,
        )

        checkpoint_dir = os.path.join(self.config.root_dir, "checkpoints")
        os.makedirs(checkpoint_dir, exist_ok=True)

        last_checkpoint = None
        checkpoint_files = sorted(
            [f for f in os.listdir(checkpoint_dir) if f.startswith("checkpoint-")],
            key=lambda x: int(x.split("-")[-1]) if x.split("-")[-1].isdigit() else 0
        )
        
        if checkpoint_files:
            last_checkpoint = os.path.join(checkpoint_dir, checkpoint_files[-1])
            print(f"Resuming training from checkpoint: {last_checkpoint}")
        else:
            print("No checkpoint found, training from scratch...")
        

        #Setting up the training argumets: Reading the paramters from params.yaml:
        trainer_args = TrainingArguments(
            output_dir = os.path.join(self.config.root_dir,"checkpoints"),
            num_train_epochs = self.config.num_train_epochs,
            warmup_steps = self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay= self.config.weight_decay,
            logging_steps=self.config.logging_steps*2, 
            evaluation_strategy="steps",
            eval_steps=self.config.eval_steps,
            save_strategy = "steps",
            save_steps = 25,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            save_total_limit=2,
            report_to = "none",
            load_best_model_at_end=True,
            remove_unused_columns=False
        )

        # Initialising the trainer:
        trainer = Trainer(
            model = model_pegasus,
            args = trainer_args,
            tokenizer = tokenizer,
            data_collator= seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset= dataset_samsum_pt["validation"])
        
        #Training the trainer:
        trainer.train(resume_from_checkpoint = last_checkpoint)

        #Saving the model:
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))

        #Saving the tokenizer:
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
    