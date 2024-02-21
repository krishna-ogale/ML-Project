import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.debug('This is a debug message')  # This won't be logged because level is INFO
logging.info('This is an info message')    # This will be logged
logging.warning('This is a warning message')  # This will be logged
logging.error('This is an error message')    # This will be logged
logging.critical('This is a critical message')  # This will be logged

