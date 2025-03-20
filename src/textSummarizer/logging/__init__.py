#Here we will create our own custom log:
import os
import sys
import logging

#Defining a custom logging string:
#asctime -> Timestamp for log
#levelname -> Level of the log
#module -> Source module in which the change has taken place
#message -> logging message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Creating the folder for logs:
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok = True)

#Logic for logging the changes:
logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        #For logging into a file:
        logging.FileHandler(log_filepath),

        #For showing the logs into the terminal:
        logging.StreamHandler(sys.stdout)
    ]
)

#Definig the custom logger:
logger = logging.getLogger("textSummarizerLogger")

