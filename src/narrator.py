# 2017-02-07 

import string
import os, sys
import logging

logger = logging.getLogger('explorer.narrator')

def narrate():
    ''' Stubby function to accept user input and quit when asked '''
    logger.info('Beginning narrate function')
    print "Welcome! Type 'quit' at any time to stop the program."
    while True: 
        user_input = raw_input('> ')
        parsed_input = parse(user_input)
        logger.info('Parsed input: {}'.format(parsed_input))
        if parsed_input is None:
            logger.info('User has specified no command words')
            continue
        elif len(parsed_input) > 1: 
            logger.info('{} commands were received!'.format(len(parsed_input)))
            priority_order = ['quit','help','look','go','verbose']
            parsed_priorities = [priority_order.index(x) for x in parsed_input]
            action = priority_order[min(parsed_priorities)]
            logger.info('Highest priority is {}'.format(action))
        elif len(parsed_input) == 0: # something went wrong
            logger.error('An empty list of commands was returned.')
        else: # one command was returned
            action = parsed_input[0]
        # now to execute these actions
        if action == 'look':
            logger.info('User wants to look around')
            look(os.getcwd())
        elif action == 'help':
            logger.info('User has asked for help')
            print("Feeling lost? Available commands are 'look' (look at current directory) and 'go' (move to another directory). Type 'quit' at any time to stop.")
        elif action == 'go':
            logger.info('User wants to move to a different directory')
            print("Haha, this is embarrassing, I haven't coded that yet.")
        elif action == 'quit':
            logger.info('User has chosen to exit')
            print('Goodbye!')
            break
        else:
            logger.info('Something else has happened: user said {} and it was parsed into {}'.format(user_input, parsed_input))
            print('How funny!')

def parse(input):
    ''' Processes the raw user input and returns a list of canonical
    command word(s) from a large number of possible synonyms '''
    commands = {'quit': ['quit','exit','leave','goodbye','bye','q'], \
                'look': ['look','examine'], \
                'help': ['help','options','menu','h'], \
                'verbose': ['verbose','debug','v'], \
                'go': ['go','enter','ls','list','dir','move']}
    # flattened list of all command dictionary values
    all_commands = [x for y in commands.values() for x in y]
    # now identify dict keys for all command words in user input
    word_list = input.lower().translate(None, string.punctuation).split()
    logger.debug('Processed word list: {}'.format(word_list))
    command_input = [x for x in word_list if x in all_commands]
    if len(command_input) == 0:
        logger.info('No commands found')
        return None
    else:
        # generate inverse dictionary 
        # (Note that efficiency is a non-concern right now)
        tuple_pairs = [[(v[v.index(i)], k) for i in v] for k, v in commands.items()]
        flattened_tuples = [x for y in tuple_pairs for x in y]
        inverse_commands = dict(flattened_tuples)
        core_commands = [inverse_commands[i] for i in command_input]
        return core_commands
    
def look(path):
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

if __name__ == '__main__':
    narrate()
