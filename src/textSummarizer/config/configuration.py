# Import all the constants:
from src.textSummarizer.constants import *

# Import necessary file from commonly used functions:
from src.textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)

#Creating a class of configuration Manager:
class ConfigurationManager:

    #Defining a constructor with following paramteres:
    def __init__(self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):

        #Obtaining the config from the file_path:
        self.config = read_yaml(config_filepath)
        
        #Obtaining the paramters from the file_path:
        self.params = read_yaml(params_filepath)

        #Creating a new artifact: root folder:
        create_directories([self.config.artifacts_root])

    #Defining a function to get the data ingestion config:
    def get_data_ingestion_config(self) -> DataIngestionConfig:

        #Obtaining all the values of the current object:
        config = self.config.data_ingestion

        #Creating a directory for the root directory of the current config:
        create_directories([config.root_dir])

        #Setting up all the values of class:
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )


        return data_ingestion_config
    
    
    #Defining a function to get the data Validation config:
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    
    
    #Defining a function to to get data tranformation configuration:
    def get_data_tranformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_tranformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )

        return data_tranformation_config
    
    #Defining the function for obtaining the model trainer config:
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        #Obtaining the configuration:
        config = self.config.model_trainer

        #Obtaining the parameters:
        params = self.params.TrainingArguments

        #Creating a directory storing the configuration root directory:
        create_directories([config.root_dir])

        #Creating the model_trainer config:
        model_trainer_config = ModelTrainerConfig(

            #Setting up all the values:
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps= params.eval_steps,
            save_steps=max(1,(params.eval_steps*((params.num_train_epochs//10) or 1))),
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            per_device_eval_batch_size=params.per_device_eval_batch_size,
        )

        return model_trainer_config
    
    #Defining a function to Obtain model evaluation:
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        #Obtaining the configuration of the current model:
        config = self.config.model_evaluation

        #Creating directory:
        create_directories([config.root_dir])

        #Defining model evaluation configuration:
        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
        )

        #Returning the Model Evaluation config:
        return model_evaluation_config
