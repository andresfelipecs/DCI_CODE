import re

def run():

    print('Task 1 ')

    text = 'Berlin is a world city of culture, politics, media and science.'

    pattern = '\s'
    # <re.Match object; span=(6, 7), match=' '>
    location = re.search(pattern, text)

    # span() returns both start and end indexes in a single tuple.
    loc_in = location.span()
    print(loc_in)
    print('The first white-space character is located at position: ', loc_in[0], '\n')

    print('Task 2 ')

    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

    finder = re.search('Frankfurt', text)

    print(finder, '\n')

    print('Task 3 ')

    text = 'Berlin is a city of culture.'

    change = re.sub(' ', '-', text)

    print(change, '\n')

    print('Task 4 ')

    text = 'Berlin is a city of culture.'

    finder = re.search('in', text)

    print(finder, '\n')

    print('Task 5 ')

    pattern = '\AB\w+'

    position = re.search(pattern, text)

    pos_ind = position.span()

    print(pos_ind, '\n')

    print('Task 6 ')

    text = 'The rain in Spain.'

    finder = re.findall('ai', text)

    print(len(finder), '\n')


if __name__ == '__main__':
    run()