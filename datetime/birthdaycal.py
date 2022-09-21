from datetime import datetime, timedelta


def birthday():

    birthday_date = input('\n Enter your birthday (exp: 1995 04 22) : \n ')
    #birthday_date = '1995 04 22'
    p = datetime.strptime(birthday_date, "%Y %m %d")
    time_now = datetime.now()
    diff = time_now - p
    years = diff.days / 365
    months = diff.days / 31
    weeks = diff.days / 7
    #print(diff)

    print( f' Since {birthday_date} have passed: \n {int(years)} years {int(months)} months {int(weeks)} weeks {diff.days} days \n')

if __name__ == "__main__":
    birthday()