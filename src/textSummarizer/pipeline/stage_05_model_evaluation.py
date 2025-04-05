from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger

#Creating a class for evluating training pipeline:
class ModelEvaluationTrainingPipeline:

    #Constructor: Doing nothing:
    def __init__(self):
        pass

    #main function:
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
        model_evaluation_config.evaluate()