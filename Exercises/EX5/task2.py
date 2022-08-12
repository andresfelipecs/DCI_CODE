def run():
    print('Hi, please enter two digits to get their difference :) ')
    for i in range(3):
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))
        result = number1 -number2
        if number1 > number2:
            result = result * 2
        else:
            result = abs(result)
        print('The result of calculation is  ')



if __name__ == '__main__':
    run()