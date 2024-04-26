import logging
import os

#To get logs, we should get the root directory here
from from_root import from_root
from datetime import datetime

#Whenever we run the pipeline again,it should create a new log file
#Log file name will be month_date_year_hour_min_second.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'
#These log files which will be created will be stored in folder name logs
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

#If logs folder already exists then it will not create, else it will create the folder
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,   #Everything about debug will be logged and written in this file
)