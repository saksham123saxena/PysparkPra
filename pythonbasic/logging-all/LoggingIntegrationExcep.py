import logging
import os
'''
exc_info=True ::-->> use for printing Traceback information
'''
try:
    print(sal)
except Exception as exp:
    logging.basicConfig(level=logging.ERROR,filename='TestingFile1.log',filemode='w',
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging.error("Logging error "+str(os.name)+" -->> ",exc_info=True)

