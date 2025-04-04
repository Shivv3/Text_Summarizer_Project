from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger

#Creating a class for data Transformation training pipeline:
class ModelTrainerPipeline:

    #Constructor: Doing nothing:
    def __init__(self):
        pass

    #main function:
    def main(self):
        #Intialising the configuration manager:
        config = ConfigurationManager()

        #Obtaining the model configuration:
        model_trainer_config = config.get_model_trainer_config()

        #Applying the model_trainer_config into model_trainer object:
        model_trainer_config = ModelTrainer(config = model_trainer_config)

        #Calling the train function:
        model_trainer_config.train()