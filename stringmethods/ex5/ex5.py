def inatorInator(word):
        con = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q' 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
        if word.endswith(con):
            word2 = word + 'inator' + ' '+ str(len(word)) + '000'
            print('inatorInator'+'('+ word +')'+' ➞ '+ word2)
        else:
            word2 = word + '-inator' + ' '+ str(len(word)) + '000'
            print('inatorInator'+'('+ word +')'+' ➞ '+ word2)





def run():
    for i in range(3):
        word = input(str('Enter single word string: '))
        inatorInator(word)


if __name__ == '__main__':
    run()   
