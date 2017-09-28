# Started: 2017-03-30
import logging
import filesystem_utils as f
import narrator as n
import utils as u

# Logging config
logger = logging.getLogger('explorer')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('{0}%(asctime)s{1} %(levelname)s - {0}%(message)s{1}'.format(u.colors['gray'], u.colors['default'], u.colors['black']), '%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.info('Initialized logging')
    n.narrate()

    
