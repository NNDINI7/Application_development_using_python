# Logging to output streamer/file 
#stream : output console vr disayla hv

import logging
logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

dev_file_handler = logging.FileHandler("app_dev.log")
logger.addHandler(dev_file_handler)

test_file_handler = logging.FileHandler("app_test.log")
logger.addHandler(test_file_handler)

logger.info("Info msg passed to handler.")
logger.critical("critical msg passed to handler.")
logger.debug("debug msg passed to handler.") #debug will not get print 
