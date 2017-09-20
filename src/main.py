# Started: 2017-03-30
import logging
import filesystem_utils as f
import narrator as n

# ANSI color escape sequences (foreground only), used with string formatting 
# to color logging output in a more readable way.
colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'default': '\033[0m',
    'gray': '\033[38;5;247m',
}

# Logging config
logger = logging.getLogger('explorer')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('{0}%(asctime)s{1} %(levelname)s - {0}%(message)s{1}'.format(colors['gray'], colors['default'], colors['black']), '%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.info('Initialized logging')
    n.narrate()

    
