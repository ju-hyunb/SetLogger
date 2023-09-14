#-*- coding:utf-8 -*-

import os
import logging
import logging.config
import json


PATH = os.path.join(os.path.dirname(__file__), 'logger.json')
CONFIG = json.load(open(PATH))

def get_logger(script_name, levels):
    

    CONFIG['loggers']['root']['handlers'] = []
    for level in levels:
        CONFIG['handlers'][f'file_{level}']['filename'] = script_name + '.' + CONFIG['handlers'][f'file_{level}']['filename']
        CONFIG['loggers']['root']['handlers'].append(f'file_{level}')


    loglevel = ["debug", "info", "warn", "error", "exception"]
    for level in loglevel:
        if level not in levels:
            del CONFIG["handlers"][f"file_{level}"]


    logging.config.dictConfig(CONFIG)
    return logging.getLogger(__name__)




class Log:
    def __init__(self, msg):
        self.msg=msg

    def debug(self):
        logging.debug(self.msg)
    def info(self):
        logging.info(self.msg)
    def warn(self):
        logging.warn(self.msg)
    def error(self):
        logging.error(self.msg)
    def exception(self):
        logging.exception(self.msg, exc_info=self.msg)


    



