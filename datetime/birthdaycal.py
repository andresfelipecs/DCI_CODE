from datetime import datetime


def birthday():

    birthday_date = input('\n Enter your birthday (exp: YYYY MM DD) :    ') # enter input
    #birthday_date = '1995 04 22'
    c = datetime.strptime(birthday_date, "%Y %m %d") # convert input into daytime object
    time_now = datetime.now() # set a variable with the current date 
    diff = time_now - c # find the difference between the current time and the birthday
    years = diff.days / 365 # the difference in days / 365 gives us the year
    months = years * 12 # the years multiply by 12 gives us the months 
    weeks = diff.days / 7 # and the difference in days divided by 7 gives us the weeks
    # everything you can find it with the rule of 3

    print( f'\n Since {birthday_date} have passed: \n {years} years, {months} months, {weeks} weeks, and {diff.days} days \n')


    print(type(diff))
if __name__ == "__main__":
    birthday()