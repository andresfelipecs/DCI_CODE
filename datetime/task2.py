from datetime import datetime, timedelta, date
from hashlib import new
from time import sleep


def run():

    current_datetime = datetime.now()
    print('Current date: \n', current_datetime)

    sleep(0.8)

    print('\n TASK 1')
    
    delta = timedelta(days=15)
    less_15 = current_datetime - delta
    
    print(less_15)

    sleep(0.8)

    print('\n TASK 2')

    delta = timedelta(days=7)
    more_7 = current_datetime + delta
    
    print(more_7)

    sleep(0.8)

    
if __name__ == '__main__':
    run()