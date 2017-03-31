# 2017-02-07 

import string
import os, sys

def narrate():
    ''' Stubby function to accept user input and quit when asked '''
    quit_words = ['quit', 'exit']
    print "Welcome! Type 'quit' at any time to stop the program."
    while True: 
        user_input = raw_input('> ')
        parsed_input = parse(user_input)
        print parsed_input
        if 'look' in user_input.lower().split():
            look()
        if 'help' in user_input.lower().split():
            print "Feeling lost? Type 'quit' at any time to stop."
        if user_input.lower() in quit_words:
            print 'Goodbye!'
            break

def parse(input):
    ''' Performs some basic string manipulation and returns result '''
    commands = {'quit': ['quit','exit','leave','goodbye','bye'], \
                'look': ['look', 'examine'], \
                'help': ['help', 'options', 'menu'], 'verbose': ['verbose', 'debug'], \
                'go': ['go', 'enter', 'ls', 'list', 'dir']}
    word_list = input.lower().translate(None, string.punctuation).split()
    return word_list
    
def look(p='.'):
    ''' Prints out the files and directories '''
    result = os.listdir(p)
    dirs = os.walk(p).next()[1]
    files = os.walk(p).next()[2]
    print 'You see some files: {}'.format(files)
    print 'You can go: {}'.format(dirs)

if __name__ == '__main__':
    narrate()
    
