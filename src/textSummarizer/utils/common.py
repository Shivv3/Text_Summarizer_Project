#What are 'utils':
"""
If you are using any python function frequently in your code. This frequently used function can be written in this 'utils' instead of the component section
and whenever needed, You just import it from utils.
These frequently used functions are called utility functions.
"""

#Importing the libraries necessary:
import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#A commonly used function to read a yaml file:
#ensure_annotations: It ensures that the datatype of the arguments are maintained/preserved while using the function.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: If yaml file is empty:
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


#A method to create directories:
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """The function create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    #Traversing over all the list of all the directory paths:
    for path in path_to_directories:

        #Creating the ith directory:
        os.makedirs(path,exist_ok=True)

        if verbose:
            logger.info(f"created directory at: {path}")

#A method to get the size of a file stored at the path:
@ensure_annotations
def get_size(path: Path) -> str:
    """The function gets the size of the file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    #Obtaining the size of the file in KB:
    size_in_kb = round(os.path.getsize(path)/1024)

    #Returning the size:
    return f"~ {size_in_kb} KB"

