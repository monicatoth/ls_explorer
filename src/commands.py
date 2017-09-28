# started: 2017-09-20
from __future__ import print_function
import string
import os, sys
import subprocess # to get terminal size
import logging
import utils as u

logger = logging.getLogger('explorer.narrator')

# all commands and synonyms
commands = {'quit': ['quit','exit','leave','goodbye','bye','q', 'stop'], \
            'look': ['look','examine', 'ls', 'list', 'dir'], \
            'help': ['help','options','menu','h'], \
            'verbose': ['verbose','debug','v'], \
            'go': ['go','enter','cd','move', 'walk', 'n', 's', 'e', 'w'], \
            'where': ['where','pwd'], \
            'inventory': ['inventory', 'i', 'stuff', 'possessions']}

def extract_commands(input):
    ''' Processes the raw user input and returns a list of canonical
    command word(s) from a large number of possible synonyms; runs this
    list through a prioritization function to return a single command 
    to execute'''
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
    priority_order = ('quit','help','look','go','verbose','inventory')
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
    ''' Calls the function to execute a specific action and performs any 
    other necessary tasks (none yet, but I'm sure I'll think of something) '''
    # when zero arguments are needed: 
    if action in ('help', 'quit', 'inventory'):
        correct_function = globals()['execute_{}'.format(action)]
        correct_function()
    # when one argument is needed: 
    elif action == 'look':
        correct_function = globals()['execute_{}'.format(action)]
        correct_function(rest_of_text=raw_user_input)
        #print("Feeling lost? Available commands are 'look' (look at current directory) and 'go' (move to another directory). Type 'quit' at any time to stop.")
    elif action == 'where':
        logger.info('User wants an action that is only a placeholder at present')
        print("Haha, this is embarrassing, I haven't coded that yet.")
    elif action == 'go':
        correct_function = globals()['execute_{}'.format(action)]
        correct_function(rest_of_text=raw_user_input)
    else:
        logger.info("We recognize this as a command but don't know what to do about it: {}".format(action))
        print("Sorry! I don't know what to tell you.")

def execute_inventory():
    print('You check your inventory. You have: a stick of gum, a business card, a pair of scissors. I have not programmed any actions you can take with any of these items.')

def execute_quit():
    logger.info('User has chosen to exit')
    print('Goodbye!')
    sys.exit(0)

def execute_help():
    ''' Returns a string that lists all recognized functions and a brief 
    description of each. '''
    logger.info('Beginning help function')
    commands = {'look': 'look at current directory', 'go': 'move to another directory', 'quit': 'exit to the command line'}
    first_line = "Feeling lost? Available commands are:"
    command_output = '\n'.join(['{0:5}{1}{2:10}{3}{4}'.format
                                ('', u.colors['red'], x, u.colors['default'],
                                 commands[x]) for x in commands.keys()])
    print('\n'.join([first_line, command_output]))

def format_list(l, column_num=0):
    ''' Recursive function; takes a list (e.g. of files) and returns a 
    multi-line string with the list items nicely padded by empty space'''
    if len(l) < 5 and column_num < 1:
        # short lists are easy; we use just one column
        # unless we have specified our column_num for some reason
        padded_list = ['    {}'.format(x) for x in files]
        return '\n'.join(padded_list)
    else:
        rows, columns = [int(x) for x in 
                         subprocess.check_output(['stty', 'size']).split()]
        line_list = []
        longest_item = max([len(x) for x in l])
        if column_num < 1: # then we have not already called this function!
            # we begin with the assumption that we'll have two columns for
            # lists under 10 items, and three columns otherwise.
        else:
            # column_num's word is law
            spacing = longest_item + 4
            i = 0
            while i < len(l):
                if i + column_num > len(l):
                    single_row = l[i:]
                else:
                    single_row = l[i:i+column_num]
                format_string = ['{:<{fill}}' for x in single_row]
                line_list.append(''.join(format_string).format(*single_row, fill=spacing))
                i = i + column_num
                
                
            
    
    
def execute_look(path=os.getcwd(), rest_of_text=None):
    ''' Prints out the files and directories '''
    rows, columns = [int(x) for x in 
                     subprocess.check_output(['stty', 'size']).split()]
    logger.info('User wants to examine {}'.format(path))
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    if len(files) < 1:
        print('There are no files here.')
    else:
        files.sort()
        # figure out the spacing - then put this in a helper function
        longest_file = max([len(x) for x in files])
        if len(files) > 6: # three columns, four spaces
            # format will go: ___file1___file2___file3___
            # make sure there are at least four spaces between files
            column_num, space_num = 3, 4
            if (longest_file + 4) <= columns/3:
                pass
            else:
                columns = 2
            while i < len(files):
                space_length = (columns - len(''.join(files[0:b])))/space_num
                if space_length > 4:
                    # fix this later
                    first_line = '{a:<{fill}}{b:<{fill}}'.format(a=files[0], b=files[1], fill=space_length)                    
            # find difference between 
        while x < columns:
            # fill this in
            break
        print('You see some files: {}'.format(files))
    if len(dirs) < 1:
        print('You can go: back the way you came')
    else:
        print('You can go: {}'.format(dirs))

def execute_go(path=os.getcwd(), rest_of_text=None):
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
