# 2017-02-07 

import os, sys

def narrate():
    ''' Stubby function to accept user input and quit when asked '''
    quit_words = ['quit', 'exit']
    print "Welcome! Type 'quit' at any time to stop the program."
    while True: 
        user_input = raw_input('> ')
        if 'look' in user_input.lower().split():
            look()
        if 'help' in user_input.lower().split():
            print "Feeling lost? Type 'quit' at any time to stop."
        if user_input.lower() in quit_words:
            print 'Goodbye!'
            break
        else:
            print 'You just said: {}'.format(user_input)

def look(p='.'):
    ''' Prints out the files and directories '''
    result = os.listdir(p)
    dirs = os.walk(p).next()[1]
    files = os.walk(p).next()[2]
    print 'You see some files: {}'.format(files)
    print 'You can go: {}'.format(dirs)

if __name__ == '__main__':
    narrate()
    
