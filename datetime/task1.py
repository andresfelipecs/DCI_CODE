from datetime import datetime

def run():

    print('TASK 1')

    current_datetime = datetime.now()

    weekday = current_datetime.weekday()
    print(weekday)


    print('TASK 2')

    some_date = datetime(2021, 7, 14)

    weekday2 = some_date.weekday()
    print(weekday2)

    print('TASK 3')

    # Go to leap_year.py 

    print('TASK 4')

    date_as_string = "Feb 14 2021 8:30AM"

    con = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
    print(con)

if __name__ == '__main__':
    run()