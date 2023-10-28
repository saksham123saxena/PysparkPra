'''
setting the logging level
'''

import logging
logging.basicConfig(level=logging.DEBUG)  # way of setting level

logging.debug("this is for debug")
logging.info("this is for info")
logging.error("this is for error")
logging.warning("this is for warning")
logging.critical("this is for critical")

