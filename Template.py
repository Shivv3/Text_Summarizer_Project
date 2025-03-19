import os
from fileinput import filename
from pathlib import Path
import logging

# Creating a logging stream to keep the track of Information related logs:
logging.basicConfig(level = logging.INFO,format = '[%(asctime)s]: %(message)s:')

# Specifying the project name:
project_name = "textSummarizer"

# Specifying the list of files and folders:
"""
The following folders I will be needing:
1. .github folder: This folder is used when we will be deploying our project: Here we write CI/CD related EML file
2. src folder: A constructor file is needed '__init__.py' to install this file in my local package. Whenever this constructor file is present that folder is considered as my local package.
3. components inside the src folder
4. utils inside the src folder
5. research contains all the documentation and notebook experiments.
and many more.. we will talk about.
"""
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Code for specifying how the template files will be created:
for filepath in list_of_files:

    # We convert the filepath according to the OS we are using like windows/linux:
    filepath = Path(filepath)

    # From the path we need to separate out my folders and files: We separate the folder from the files inside it.
    fileDirectory,fileName = os.path.split(filepath)

    #CODE FOR CREATING A FILE DIRECTORY:
    # If the file directory is not empty:
    if fileDirectory != "":

        #Making the directory if it does not exist:
        os.makedirs(fileDirectory, exist_ok = True)

        #Logging the information for creating the directory:
        logging.info(f"Creating directory: {fileDirectory} for the file {fileName}")

    # CODE FOR CREATING A FILE:
    # If the file does not exist in the directory or if the file size is 0:
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):

        # Opening the file in the writing mode just for the sake of creating it:
        with open(filepath,'w') as f:

            #Once the file is created: We do nothing inside it:
            pass

            #Logging the information that a new file is created:
            logging.info(f"Create an empty file: {filepath}")

    # If the file already exist in the directory:
    else:

        #logging the information that the file already exist:
        logging.info(f"{filename} already exist in the directory")
