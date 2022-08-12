# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

def run():
    print('Hi, please enter the numbers that you want to sum: ')
    for i in range(2):
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))
        number3 = int(input('Third number: '))
        result = number1 + number2 + number3
        if number1 == number2 == number3:
            result = result * 3 
            print('the triple sum is: ', result)
        else:
            print('The sum is: ',result, '\n')


if __name__ == '__main__':
    run()