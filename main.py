#Importing the Stage_01_Data_Ingestion:
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

#Defining the stage name:
STAGE_NAME = "Data Ingestion Stage"
try:
    #Logging for the stage name starting
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")

    #Initialising the data Ingestion training pipeline object:
    data_ingestion = DataIngestionTrainingPipeline()

    #Calling the main function of the data ingestion object:
    data_ingestion.main()

    #Logging the stage name completion:
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e