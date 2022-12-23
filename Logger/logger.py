import logging
import inspect, sys
import logger as log
from datetime import datetime



# VARIABLE DECLARATION
recordLogs = True
filePath = './logs/' + str(datetime.now().strftime("log_%m-%d-%Y_%H-%M-%S")) + '.txt'


logging.basicConfig (
                        level=logging.DEBUG,
                        format='%(asctime)s%(msecs)03d - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=filePath,
                        filemode='w'
                    )


# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(message)s')
# formatter.default_msec_format = '%s.%0d'
# console.setFormatter(formatter)
# logging.getLogger('LoggerInit').addHandler(console)
# LoggerInit = logging.getLogger('LoggerInit')
# LoggerInit.info(f'\t{"#" * 20} @ Compiled')



def LogUpd(msg='', recordLog = cnfg.GetConfig('logger')['record_logs']):
    if recordLog == True:
        srcFile = inspect.getsourcefile(sys._getframe(1))
        loggerName = srcFile.split('/')
        logging.getLogger(loggerName[len(loggerName)-1]).addHandler(console)
        logging.getLogger(loggerName[len(loggerName)-1]).info(msg)