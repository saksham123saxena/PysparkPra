import logging

# --:: use for only for one filemode='w'
# logging.basicConfig(level=logging.DEBUG, filename='TestingFile.log',filemode='w')
# logging.debug("this is debug logging level for TestingFile !!")


logging.basicConfig(level=logging.DEBUG, filename='TestingFile.log',filemode='w',
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("this is debug logging level for TestingFile !!")
