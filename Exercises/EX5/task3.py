def run():
    print("let's check if the numbers are even or odd")
    for i in range(2):
        number = int(input('number to check: '))
        if number %2 == 0:
            print(number,' is an even number! ', '\n')
        else:
            print(number, ' is an odd number! ', '\n')

if __name__ == '__main__':
    run()
