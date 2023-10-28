import logging

logger = logging.getLogger(__name__)

f_handler=logging.FileHandler("TestingCustomLogger.log",mode='w')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(f_handler)
logger.error("this is custom logger - handler")
