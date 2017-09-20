# started: 2017-09-20
from __future__ import print_function
import string
import os, sys
import logging
import ansi_colors as ansi

logger = logging.getLogger('explorer.narrator')

def extract_commands(input):
    ''' Processes the raw user input and returns a list of canonical
    command word(s) from a large number of possible synonyms; runs this
    list through a prioritization function to return a single command 
    to execute'''
    # todo: put commands and synonyms in other file; import from there
    commands = {'quit': ['quit','exit','leave','goodbye','bye','q'], \
                'look': ['look','examine', 'ls', 'list', 'dir'], \
                'help': ['help','options','menu','h'], \
                'verbose': ['verbose','debug','v'], \
                'go': ['go','enter','cd','move', 'walk'], \
                'where': ['where','pwd']}
    # flattened list of all command dictionary values
    all_commands = [x for y in commands.values() for x in y]
    # now identify dict keys for all command words in user input
    word_list = input.lower().translate(None, string.punctuation).split()
    logger.debug('Processed word list: {}'.format(word_list))
    command_input = [x for x in word_list if x in all_commands]
    if len(command_input) == 0:
        return None
    else:
        # generate inverse dictionary 
        # (Note that efficiency is a non-concern right now)
        tuple_pairs = [[(v[v.index(i)], k) for i in v] for k, v in commands.items()]
        flattened_tuples = [x for y in tuple_pairs for x in y]
        inverse_commands = dict(flattened_tuples)
        core_commands = [inverse_commands[i] for i in command_input]
    if len(core_commands) == 1:
        logger.info("One command found: '{}', which is identical or synonymous with '{}'".format(command_input[0], core_commands[0]))
        return core_commands[0]
    else:
        prioritized = prioritize_commands(tuple(core_commands))
        return prioritized

def prioritize_commands(input):
    ''' Receives a tuple of one or more commands; returns the highest priority
    command as a string '''
    priority_order = ('quit','help','look','go','verbose')
    # Manage cases of poor input hygiene:
    if len(input) < 2:
        if len(input) == 1:
            return input[0]
        elif len(input) == 0 or input is None:
            logger.error('Received an empty or null list of commands to prioritize')
            return None
        else: # something extremely weird has happened
            logger.error('We should never see this error. Something unexpected happened while trying to prioritize these commands: {}'.format(input))
            return None
    # In the expected case (where the list is 2+ items long):
    command_priorities = tuple(sorted(input, key=priority_order.index))
    logger.info('{} commands found: {}, prioritized in this order: {}'.format(len(input), input, command_priorities))
    return (command_priorities[0])

def execute_command(action, raw_user_input=None):
    if action == 'look':
        logger.info('User wants to examine current directory')
        look(rest_of_text=raw_user_input)
    elif action == 'help':
        logger.info('User has asked for help')
        help_output = execute_help()
        print(help_output)
        #print("Feeling lost? Available commands are 'look' (look at current directory) and 'go' (move to another directory). Type 'quit' at any time to stop.")
    elif action == 'where':
        logger.info('User wants an action that is only a placeholder at present')
        print("Haha, this is embarrassing, I haven't coded that yet.")
    elif action == 'go':
        move_path(rest_of_text=raw_user_input)
    elif action == 'quit':
        logger.info('User has chosen to exit')
        print('Goodbye!')
        sys.exit(0)
    else:
        logger.info("We recognize this as a command but don't know what to do about it: {}".format(action))
        print("Sorry! I don't know what to tell you.")

def execute_help():
    ''' Returns a string that lists all recognized functions and a brief 
    description of each. '''
    logger.info('Beginning help function')
    commands = {'look': 'look at current directory', 'go': 'move to another directory', 'quit': 'exit to the command line'}
    first_line = "Feeling lost? Available commands are:"
    command_output = '\n'.join(['{0:5}{1}{2:10}{3}{4}'.format
                                ('', ansi.colors['red'], x, ansi.colors['default'],
                                 commands[x]) for x in commands.keys()])
    return '\n'.join([first_line, command_output])
    
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
