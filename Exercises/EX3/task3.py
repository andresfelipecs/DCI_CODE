def run():
    
    number = int(input('Enter number: '))
    for i in range(2,number+1):
        if number %i == 0:
            print(i)

if __name__ == '__main__':
    run()