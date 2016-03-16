# Started: 2/20/2016
# These are functions to return information about the directory tree and its files;
# formatting and organizing this info is done elsewhere. 
# This will be in Python for prototyping purposes, and then I expect to rewrite it in C or something.

import os, path, stat
import datetime
import argparse

# Custom errors
# -------------------------------------------------
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PathError(Error):
    """Errors arising from invalid filepaths."""
    def __init__(self, message):
        self.message = message

# Argument Parsing 
# -------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default=os.getcwd(), help='Directory path to examine')
args = vars(parser.parse_args())

# Main code
# -------------------------------------------------
def fetch_path_info(path=args['path'], topdown=True, levels=1):
    '''Get the file and directory info for a given path, with options for greater depth either top-down or bottom-up'''
    walk_data = os.walk(path, topdown)
    if list(walk_data) == []:
        specify_path_error(path)
    else:
        print list(walk_data)

def specify_path_error(path):
    '''If path is invalid, os.walk returns an empty list. Raise PathError with more specific info.'''
    path_exists, path_readable = [os.access(path, x) for x in [os.F_OK, os.R_OK]] # True/False
    if not path_exists:
        raise PathError('Path does not exist, please check for errors')
    elif not path_readable:
        raise PathError('Path exists but is not readable')
    else: 
        path_is_file = stat.S_ISREG(os.stat(path)[0]) # True/False
        if path_is_file: 
            raise PathError('Path points to a file; please specify a directory')
        else: # give up
            raise PathError('Unknown error, but path does not work; sorry')



# For testing purposes
# -------------------------------------------------
if __name__ == "__main__":
    dir_info = fetch_path_info()
