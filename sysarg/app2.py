import argparse
import sys

def run():

    parser = argparse.ArgumentParser(description='The application in this file will read the command line options using argparse.')

    parser.add_argument('--f', type=str, help='first name of user')
    parser.add_argument('--l', type=str, help='last name of user')
    parser.add_argument('--a', type=int, help='age name of user')
    parser.add_argument('--fast', action="store_true", help='fast mode')


    args = parser.parse_args()

    argumentList = sys.argv[1:]

    if args.a == None:
        args.a = 100

    if args.l == None:
        args.l = 'Hanson'

    if args.f == None:
        args.f = 'Larry'

    if args.fast:
        print('\n', 'Hello ', args.f, args.l, '\n', 'I see that you have had', str(args.a+1), ' birthdays.', '\n')
        print('fast mode enabled', '\n')
            
    else:    
        print('\n', 'Hello ', args.f, args.l, '\n', 'I see that you have had', str(args.a+1), ' birthdays.', '\n')

if __name__ == '__main__':
    run()