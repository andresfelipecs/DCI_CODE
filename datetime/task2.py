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

    print('\n TASK 3')

    start_date = datetime(year=2020, month=1, day=1)
    delta = timedelta(days=24)
    # adding the days
    more_24 = start_date + delta
    print(more_24)

    # convert to string
    string = more_24.strftime('%Y-%m-%d')
    print(string, type(string))

    # converting from one format to another to pirnt it out
    new_format = datetime.strptime(string, "%Y-%m-%d").strftime('%d %B, %Y')
    print(new_format)
    print(type(new_format))

    #converting to another a timedelta format 
    new_format2 = datetime.strptime(string, "%Y-%m-%d").strftime('%d')
    print(new_format2)
    print(type(new_format2))

    delta = timedelta(new_format2)
    delta2 = timedelta(month=1)
    for i in range(12):
        final_delta= delta +delta2
        print('\n Hello Friedrich, your rent of 300 € is due on ', final_delta)

    print('\n Hello Friedrich, your rent of 300 € is due on ', new_format)


if __name__ == '__main__':
    run()