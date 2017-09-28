# Begun: 2017-02-07 
from __future__ import print_function
import string
import os, sys
import logging
import utils as u
import commands as c

logger = logging.getLogger('explorer.narrator')

def narrate():
    ''' Simple function to provide a user prompt, accept input, and pass it
    along to the functions that recognize and fulfill commands '''
    logger.info('Beginning narrate function')
    print("Welcome! Type '{0}quit{1}' at any time to stop the program. Type '{0}help{1}' to see your options.".format(u.colors['red'], u.colors['default']))
    while True: 
        user_input = raw_input('{0}> {1}'.format(u.colors['black'], u.colors['default']))
        commands = c.extract_commands(user_input)
        if commands is None:
            logger.info('User has specified no command words')
            continue
        elif len(commands) == 0: # something went wrong
            logger.error('An empty list of commands was returned.')
        else: 
            c.execute_command(commands, user_input)
            continue

def validate_path(current_path, input_text):
    ''' Returns any valid absolute path via user input '''
    # first check whether current_path is valid
    # tokenize input
    # check for full paths in input
    # check for valid paths from current directory
    return None
    
def look(path=os.getcwd(), rest_of_text=None):
    ''' Prints out the files and directories '''
    logger.info('Now preparing to narrate for {}'.format(path))
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    if len(files) < 1:
        print('There are no files here.')
    else:
        print('You see some files: {}'.format(files))
    if len(dirs) < 1:
        print('You can go: back the way you came')
    else:
        print('You can go: {}'.format(dirs))

def move_path(path=os.getcwd(), rest_of_text=None):
    ''' Changes the scope of focus to a different filepath '''
    logger.info('Now running move_path function')
    available_dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    # check to see if rest_of_text contains a file or folder
    # if file:
    # if garbage (nothing recognized):
    # if no text:
    if rest_of_text == '' or rest_of_text == ' ' or not rest_of_text:
        logger.info('User wants to move, but did not supply any further input')
        user_input = raw_input('Where do you want to move? (Type \'look\' to see available options.) ')
        if user_input.lower() == 'look':
            logger.info('User chose to look at current directory: {}'.format(path))
            look(path)
    # if directory:
    #if 
    return None
    

if __name__ == '__main__':
    narrate()
