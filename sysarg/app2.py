import argparse # import argparse library
import sys # import sys library

#def run(): # call the function
    # init the parser
parser = argparse.ArgumentParser(description='The application in this file will read the command line options using argparse.')
    #addding arguments or options
parser.add_argument('--f', type=str, help='first name of user', default='Hanson')
parser.add_argument('--l', type=str, help='last name of user', default='Lary')
parser.add_argument('--a', type=int, help='age name of user', default=100)
parser.add_argument('--fast', action="store_true", help='fast mode')


args = parser.parse_args()

    #argumentList = sys.argv[1:]
    # default var
    # if args.a == None:
    #     args.a = 100

    # if args.l == None:
    #     args.l = 'Hanson'

    # if args.f == None:
    #     args.f = 'Larry'

if args.fast:
    print('\n', 'Hello ', args.f, args.l, '\n', 'I see that you have had', str(args.a+1), ' birthdays.', '\n')
    print('fast mode enabled', '\n')
            
else:    
    print('\n', 'Hello ', args.f, args.l, '\n', 'I see that you have had', str(args.a+1), ' birthdays.', '\n')

# if __name__ == '__main__':
#     run()