# Started: 2017-03-30
import logging
import filesystem_utils as f
import narrator as n

# Logging config
# Pretty soon this will get its own conf file
logger = logging.getLogger('explorer')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.info('Initialized logging')
    files = f.fetch_path_info()
    print(files[0][2])
    print(files[0][1])

    
