import sys

def app():
    argumentList = sys.argv[1:]

    for arg in argumentList:

        if arg in ("-h", "--Help"):
            print ('\n', 'System is figuring out how to help: Please wait')
        if arg in ("-f", "--fast"):
            print ('\n','fast mode enabled','\n')
    if arg != '-f':
        print('\n', 'slow mode enabled', '\n')
    
if __name__ == '__main__':
    app()
