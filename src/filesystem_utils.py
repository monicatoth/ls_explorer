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
    '''Base class for exceptions in this module.'''
    pass

class PathError(Error):
    '''Errors arising from invalid filepaths.'''
    def __init__(self, message):
        self.message = message

# Argument Parsing 
# -------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default=os.getcwd(), type=str, help='Directory path to examine')
parser.add_argument('-l', '--levels', default=1, type=int, help='Number of directory levels to examine')
args = vars(parser.parse_args())

# Main code
# -------------------------------------------------
def fetch_path_info(path=args['path'], topdown=True, levels=1):
    '''Get the file and directory info for a given path, with options for greater depth either top-down or bottom-up'''
    upper_limit = path.count('/') + (levels - 1)
    if levels == 1: # a shortcut
        dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
        files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
        return [(path, dirs, files)] # copying os.walk format
    walk_data = os.walk(path, topdown)
    limited_walk_data = [x for x in list(walk_data) if x[0].count('/') <= upper_limit]
    return limited_walk_data

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
    for i in args.keys(): 
        print('{argname:<10s}: {argvalue}'.format(argname=i, argvalue=args[i]))
    dir_info = fetch_path_info(path=args['path'], levels=args['levels'])
    print dir_info
