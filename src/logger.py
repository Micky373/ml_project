# Importing useful libraries
import logging
import os
from datetime import datetime

# Specifying the log file and path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# Creating a directory to store the log
os.makedirs(logs_path,exist_ok=True)

# Specifying the log file after the folder creation
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Specifying the format how we want it to be written
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)