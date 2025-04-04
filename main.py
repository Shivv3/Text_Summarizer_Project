#Importing the Stage_01_Data_Ingestion:
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline

#Defining the stage name: for data ingestion:
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


#Defining the stage name: for data validation:
STAGE_NAME = "Data Validation Stage"
try:
    #Logging for the stage name starting
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")

    #Initialising the data Validation training pipeline object:
    data_Validation = DataValidationTrainingPipeline()

    #Calling the main function of the data ingestion object:
    data_Validation.main()

    #Logging the stage name completion:
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


#Defining the stage name: for data Tranformation:
STAGE_NAME = "Data Transformation Stage"
try:
    #Logging for the stage name starting
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")

    #Initialising the data Transformation training pipeline object:
    data_Transformation = DataTransformationTrainingPipeline()

    #Calling the main function of the data ingestion object:
    data_Transformation.main()

    #Logging the stage name completion:
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f"*****************")

    #Logging for the stage name starting
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")

    #Initialising the Model training pipeline object:
    model_trainer = ModelTrainerPipeline()

    #Calling the main function of the with model trainer obeject:
    model_trainer.main()

    #Logging the stage name completion:
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


