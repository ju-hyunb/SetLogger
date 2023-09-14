import os
import sys

#Setup Log
##current file name
script = os.path.basename(sys.argv[0]).replace(".py", "")

##config file path
logpath = sys.argv[1]
sys.path.append(logpath)

import SetLogger as logger
import AlertSlack as alert
logger_obj = logger.get_logger(script, ["info", "exception"])
alert.Send(logger_obj)



if __name__ == '__main__':
    
    logger.Log("Start Process").debug()

    for i in range(5):
        logger.Log(f"value is {i}").info()

        try:
            result = 5/i
            logger.Log(f"Result is {result}").info()
        except Exception as e:
            logger.Log(e).exception()
            logger_obj.error(e)


