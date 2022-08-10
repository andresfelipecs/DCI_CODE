def run():

    number = int(input('Enter number of arguments  '))

    if number == 1:
        for i in range (number):
            print('please enter another number. ')
            print('function: ', i+1)

    if number == 2:
        number1 = int(input('Enter starting number: '))
        number2 = int(input('Enter stopping number: '))
        for i in range (number1, number2):
            print(i)

    if number == 3:
        number1 = int(input('Enter starting number: '))
        number2 = int(input('Enter stopping number: '))
        step = int(input('Enter step: '))
        for i in range (number1, number2, step ):
            print(i)
            

if __name__ == '__main__':
    run()
