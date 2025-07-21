# Basic Logging 
import logging 
logging.basicConfig(level=logging.INFO)
logging.info("App Started.")


#Logging levels = NOTEST(0)/DEBUG(10)/INFO(20)/WARNING(30)/ERROR(40)/CRITICAL(50)
import logging
logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)
logging.info("This is an info message.")
logging.debug("This is a debug message!!") # we set level info i.e. 10 thus debug msg will not shown in the output.
print(logging.NOTSET,logging.INFO,logging.CRITICAL)



