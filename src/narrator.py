# 2017-02-07 

import string
import os, sys
import logging

logger = logging.getLogger('explorer.narrator')

def narrate():
    ''' Stubby function to accept user input and quit when asked '''
    quit_words = ['quit', 'exit']
    logger.info('Beginning narrate function')
    print "Welcome! Type 'quit' at any time to stop the program."
    while True: 
        user_input = raw_input('> ')
        parsed_input = parse(user_input)
        logger.info('Parsed input: {}'.format(parsed_input))
        if parsed_input is None:
            logger.info('User has specified no command words')
        elif parsed_input == 'look':
            logger.info('User wants to look around')
            look()
        elif parsed_input == 'help':
            logger.info('User has asked for help')
            print "Feeling lost? Type 'quit' at any time to stop."
        elif parsed_input == 'quit':
            logger.info('User has chosen to exit')
            print('Goodbye!')
            break
        else:
            logger.info('Something else has happened: user said {} and it was parsed into {}'.format(user_input, parsed_input))
            print('How funny!')

def parse(input):
    ''' Performs some basic string manipulation and returns result '''
    commands = {'quit': ['quit','exit','leave','goodbye','bye'], \
                'look': ['look', 'examine'], \
                'help': ['help', 'options', 'menu'], 'verbose': ['verbose', 'debug'], \
                'go': ['go', 'enter', 'ls', 'list', 'dir']}
    # flattened list of all command dictionary values
    all_commands = [x for y in commands.values() for x in y]
    # now identify dict keys for all command words in user input
    word_list = input.lower().translate(None, string.punctuation).split()
    logger.debug('Processed word list: {}'.format(word_list))
    command_input = [x for x in word_list if x in all_commands]
    if len(command_input) == 0:
        logger.info('No commands found')
        return None
    # if there are multiple commands present, pick the first one
    # time saver: if the command is the dict key and not just a value
    elif command_input[0] in commands.keys():
        logger.info('Command identified as key value: {}'.format(command_input))
        return command_input
    elif command_input[0] in all_commands:
        # this can be a one-line list comprehension later
        for item in commands.keys():
            if command_input[0] in commands[item]:
                return item
    else: # this shouldn't happen
        logger.info('No commands found, but I could have sworn there was one around here somewhere... {}'.format(command_input))
        return None
    
def look(files, dirs, path):
    ''' Prints out the files and directories '''
    logger.info('Now preparing to narrate for {}'.format(path))
    print 'You see some files: {}'.format(files)
    print 'You can go: {}'.format(dirs)

if __name__ == '__main__':
    narrate()
