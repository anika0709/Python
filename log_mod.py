import logging

logging.warning("This is a warning") # default level WARNING. default root logger, parent of every logger
logging.basicConfig(    #logging.basicConfig we are configuring the root logger
    format="[%(levelname)s]:%(lineno)s - %(message)s",
    level=logging.DEBUG
)
