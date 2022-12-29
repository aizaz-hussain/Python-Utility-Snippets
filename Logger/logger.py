import logging
import inspect, sys
import logger as log
from datetime import datetime



# VARIABLE DECLARATION
recordLogs = True
filePath = './logs/' + str(datetime.now().strftime("log_%m-%d-%Y_%H-%M-%S")) + '.txt'


logging.basicConfig (   level=logging.DEBUG,
                        filename=filePath,
                        filemode='w'  )
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                              '%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('LoggerInit').addHandler(console)



def LogUpd(msg='', level=1):

    if recordLogs == True:
        srcFile = inspect.getsourcefile(sys._getframe(1))
        loggerName = srcFile.split('/')
        logging.getLogger(loggerName[len(loggerName)-1]).addHandler(console)

        if level == 1:
            logging.getLogger(loggerName[len(loggerName)-1]).info(msg)
        elif level == 2:
            logging.getLogger(loggerName[len(loggerName)-1]).warning(msg)
        elif level == 3:
            logging.getLogger(loggerName[len(loggerName)-1]).debug(msg)
        elif level == 4:
            logging.getLogger(loggerName[len(loggerName)-1]).error(msg)