import os
import logging
import logging.config
import json


def get_logger(script_name):
    config_path = os.path.join(os.path.dirname(__file__), 'logger.json')
    config = json.load(open(config_path))
    config['handlers']['file_debug']['filename'] = script_name + '.' + config['handlers']['file_debug']['filename']
    config['handlers']['file_exception']['filename'] = script_name + '.' + config['handlers']['file_exception']['filename']
    
    logging.config.dictConfig(config)
    return logging.getLogger(__name__)



class Log:
    def __init__(self, msg):
        self.msg=msg

    def debug(self):
        logging.debug(self.msg)
    def info(self):
        logging.info(self.msg)
    def error(self):
        logging.error(self.msg)
    def exception(self):
        logging.exception(self.msg, exc_info=self.msg)


