import logging
import os,sys
from pathlib import Path

#conf
"""
This logs details.
"""
name="torswitch logger"
log_time_format="%d-%m-%Y %H:%M:%S"
formatter = logging.Formatter('%(name)s | %(levelname)s  @ %(asctime)s >> %(message)s  ',log_time_format)
path=str(Path(__file__).resolve().parent)
#log_path=path+"/log_files/"

#custom handler conf
logger=logging.getLogger(name)
logger.setLevel(logging.DEBUG)

#logging file handler 
"""
uncomment code for adding file  logging.Don't forget to add it to handler
"""
# file_handler = logging.FileHandler(log_path+"fight.log")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)

#channel handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# add handlers to logger
logger.addHandler(ch)



if __name__=="__main__":
    logger.info(f"This log is generated for pupose of testing")