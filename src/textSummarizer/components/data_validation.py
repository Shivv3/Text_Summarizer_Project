import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    #Constructor:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    #A function to validate all the files exist:
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            #Checking all the files:
            for file in all_files:

                #If the current file is not present in 'ALL_REQUIRED_FILES' of config:
                if file not in self.config.ALL_REQUIRED_FILES:

                    # Marking the Validation Status as false:
                    validation_status = False

                    #Opening the config.yaml file and write the Validaiton Status as False:
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")

                # If the current file is present in the 'ALL_REQUIRED_FILES' of config:
                else:

                    # Marking the validation status as True:
                    validation_status = True

                    #Opening the config.yaml file ans write the Validation status as True:
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")

            #Returning the Validation Status:
            return validation_status
        
        except Exception as e:
            raise e

    