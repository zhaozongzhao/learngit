import logging
import logging.config

logging.config.fileConfig("logger.conf")
logging = logging.getLogger('root')

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is debug message')
logging.error('this is error message')