from finder import Finder;
import os

def want_to_exit(str):
    return str.lower() == 'exit' or str.lower() == 'quit'

if __name__ == '__main__' : 

    while True:
        # Store user input
        words : list[str] = input('Words : ')
        # Check exit keywords
        if want_to_exit(words) : quit()

        path : str = input('Path : ')
        # # Check exit keywords
        if want_to_exit(path) : quit()

        # Verification for user inputs
        if not words : print('\nWords can\'t be empty value!')
        if not path : print('\nPath can\'t be empty value!')
        if path and words :
            if not os.path.isdir(path) :
                print('\nPath does not exist!\n') 
                continue
            break


    # Start finder with user inputs
    finder : Finder = Finder(words.split(','), path)
    finder.start()
