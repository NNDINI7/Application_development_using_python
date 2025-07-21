# Formatter and logging to a File with Rotation
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)
# Remove all existing handlers
if logger.hasHandlers():
    logger.handlers.clear()


handler = RotatingFileHandler("app.log", maxBytes=200, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info("Application started")
logging.shutdown() # ensures the close/release of all the file handlers
