import os
from pathlib import Path
from textSummarizer.entity import (DataIngestionConfig)

#Package used to download the data:
import urllib.request as request

#Package used to unzip the data after downloading:
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size

#Defining the components:
class DataIngestion:

    #constructor:
    def __init__(self,config: DataIngestionConfig):

        #Initialising the config:
        self.config = config

    #A function to download the file:
    def download_file(self):

        #If the file does not already exist in the file location:
        if not os.path.exists(self.config.local_data_file):

            #Obraining the filename and headers:
            filename, headers = request.urlretrieve(

                #Setting up the url:
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

            #Logging that the file has be downloaded:
            logger.info(f"{filename} download! with following info: \n{headers}")

        #If the file already exist in the file location:
        else:

            #Logging that the file already exist with its size:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    #A function to Extract the zip file:
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data dictionary
        Function returns None
        """

        #Obtaining the unzip path:
        unzip_path = self.config.unzip_dir

        #Creating the unzip directory:
        os.makedirs(unzip_path,exist_ok=True)

        #Extracting zip file and uploading inside my unzip folder:
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)