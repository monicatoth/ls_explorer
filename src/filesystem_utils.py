# Started: 2/20/2016
# (Worked on VERY intermittently)
# These are functions to return information about the directory tree and its files. Formatting and narrative content are found elsewhere.

import os, path
import logging
import datetime

logger = logging.getLogger('explorer.filesystem')

def test():
    logger.info('This is the test function')

def fetch_path_info(path=os.getcwd()):
    '''Get the file and directory info for a given path'''
    logger.info('Collecting file & directory info for {}'.format(path))
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    logger.info('{} directories found'.format(len(dirs)))
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    logger.info('{} files found'.format(len(files)))
    return [(path, dirs, files)] # copying os.walk format for now

if __name__ == "__main__":
    fetch_path_info()

