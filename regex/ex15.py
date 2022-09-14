import re


def run():

    list = ['5 + 2', '9 * 1', 'hello world', '123', '5 + foo']
        
    pattern = '\d+\s[\+\*\-\/]\s\d+'

    print('\n')

    for i in list:

        finder = re.search(pattern, i)

        if finder:
            print(i, '--> true')

        else: 
            print(i, '--> false')

    print('\n')

if __name__ == '__main__':
    run()