from datetime import datetime, timedelta, date
from time import sleep


def run():
    print('\n  Lets see ... \n ')

    for i in range( 1, 13):
        sleep(0.6)
        due_date = date(2020, i, 25)
        print(f"Hello Friedrich, your rent of 300 € is due on {due_date.strftime('%d %B, %Y')}")
    
    last_due = due_date + timedelta(days=31)
    print(f"Hello Friedrich, your rent of 300 € is due on {last_due.strftime('%d %B, %Y')} \n ")

if __name__ == '__main__':
    run()