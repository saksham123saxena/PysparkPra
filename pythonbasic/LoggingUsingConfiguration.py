import logging
import logging.config
import utils.config
import add

logging.config.fileConfig('utils/config/logging_config.conf')

def main():
    a,b =input("enter the value of a and b : ").split()
    output=add.add2Num(a,b)
    logging.error("Logging ended from : "+str(__name__))

if __name__ == "__main__":
    logging.error("Logging started from : "+str(__name__))
    main()
