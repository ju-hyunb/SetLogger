#!/home/jhbyun/.pyenv/shims/python3.9
#-*- coding:utf-8 -*-


import os
import logging
import logging.config
import json


def get_logger(script_name, levels):
    config_path = os.path.join(os.path.dirname(__file__), 'logger.json')
    config = json.load(open(config_path))

    config['loggers']['root']['handlers'] = []
    for level in levels:
        config['handlers'][f'file_{level}']['filename'] = script_name + '.' + config['handlers'][f'file_{level}']['filename']
        config['loggers']['root']['handlers'].append(f'file_{level}')


    loglevel = ["debug", "info", "warn", "error", "exception"]
    for level in loglevel:
        if level not in levels:
            del config["handlers"][f"file_{level}"]

 
    logging.config.dictConfig(config)
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
