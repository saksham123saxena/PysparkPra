import logging
import logging.config

logging.config.fileConfig('utils/config/logging_config.conf')

def add2Num(a,b):
    logging.error("Logging of Add class for add2Num function from : "+str(__name__))
    return a+b
