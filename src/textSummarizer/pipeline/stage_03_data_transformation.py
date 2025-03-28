from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger

#Creating a class for data Transformation training pipeline:
class DataTransformationTrainingPipeline:

    #Constructor: Doing nothing:
    def __init__(self):
        pass

    #main function:
    def main(self):
        #Initialising the configuration manager object:
        config = ConfigurationManager()

        #Obtaining the data tranformation:
        data_transformation_config = config.get_data_tranformation_config()

        # Passing the Obtained data tranformation into the Data_Tranformation Object:
        data_transformation = DataTransformation(config = data_transformation_config)

        #Calling the convert function:
        data_transformation.convert()