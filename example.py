import os
import sys

#Setup Log
##current file name
script = os.path.basename(sys.argv[0]).replace(".py", "")

##config file path
logpath = sys.argv[1]
sys.path.append(logpath)

import SetLogger as logger
logger.get_logger(script)




if __name__ == '__main__':
    
    logger.Log("Start Process").debug()

    for i in range(5):
        logger.Log(f"value is {i}").debug()

        try:
            result = 5/i
            logger.Log(f"Result is {result}").debug()
        except Exception as e:
            logger.Log(e).exception()
            