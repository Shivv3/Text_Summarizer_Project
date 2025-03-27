from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

#Creating a class for data ingestion training pipeline:
class DataIngestionTrainingPipeline:

    #Constructor: Doing nothing:
    def __init__(self):
        pass

    #main function:
    def main(self):
        #Creating a configuration manager object:
        config = ConfigurationManager()

        #Obtaining the data ingestion components:
        data_ingestion_config = config.get_data_ingestion_config()

        #Calling the data ingestion components: Intialising the components of all the data ingestion by initialising an object:
        data_ingestion = DataIngestion(config=data_ingestion_config)

        #Downloading the file:
        data_ingestion.download_file()

        #Extracting the zip_file:
        data_ingestion.extract_zip_file()