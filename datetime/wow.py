# Write a Python program to select all the Sundays of a specified year.
from datetime import date, timedelta
import os

def sundays_year():
    
    year = int(input('\n Enter the year: '))
    os.system('clear')

    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    delta = timedelta(days=1)
    days_in_year = []
    while start_date <= end_date:
        days_in_year.append(start_date)
        start_date += delta
    
    print(f'\n All Sundays in the year {year}: ')
    for i in days_in_year:
        day_name = i.strftime('%A')
        if day_name == 'Sunday':
            print(i, day_name)
        

        
            





if __name__ == '__main__':
    sundays_year()