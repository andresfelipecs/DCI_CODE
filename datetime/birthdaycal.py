from datetime import datetime


def birthday():

    birthday_date = input('\n Enter your birthday (exp: YYYY MM DD) : \n ')
    #birthday_date = '1995 04 22'
    p = datetime.strptime(birthday_date, "%Y %m %d")
    time_now = datetime.now()
    diff = time_now - p
    years = diff.days / 365
    months = years * 12
    weeks = diff.days / 7
    #print(diff)

    print( f'\n Since {birthday_date} have passed: \n {years} years, {months} months, {weeks} weeks, and {diff.days} days \n')

if __name__ == "__main__":
    birthday()