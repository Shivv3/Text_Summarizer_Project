from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

#Creating a class for data validation training pipeline:
class DataValidationTrainingPipeline:

    #Constructor: Doing nothing:
    def __init__(self):
        pass

    #main function:
    def main(self):
        # Intialising the Configuration manager:
        config = ConfigurationManager()

        #Obtaining the Data Validaiton function from the Configuration Manager Object:
        data_validation_config = config.get_data_validation_config()

        #Passing the Data_Validation_Config in dataValidaiton class:
        data_validation = DataValidation(config=data_validation_config)

        #Using the object of Data Validation: We are Validating all the files which exist:
        data_validation.validate_all_files_exist()