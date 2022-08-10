def run():
    for number in range(1000,2000):
        if number %7 == 0 and number %5 != 0:
            print(number) 


if __name__ == '__main__':
    run()