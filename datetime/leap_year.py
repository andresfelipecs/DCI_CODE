from datetime import datetime

def run():

    print('Lets check if the year is a leap year or not')
    year = int(input('Enter year: \n'))

    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} is a common year')
        else:
            print(f'{year} is a leap year')  

    else:
        print(f'\n {year} is a common year')



if __name__ == '__main__':
    run()