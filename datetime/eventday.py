from datetime import datetime, timedelta


def event():# define function event

    event_date = input("Enter the event date (YYYY MM DD):   ") # enter the date
    c = datetime.strptime(event_date, "%Y %m %d") # convert the from str to datetime object
    time_now = datetime.now() # set a variable with the current date 
    diff = c - time_now # find the difference between the current time and the event  
    print(diff, type(diff))
    years = diff.days / 365 # the difference in days / 365 gives us the year
    months = years * 12 # the years multiply by 12 gives us the months 
    weeks = diff.days / 7 # and the difference in days divided by 7 gives us the weeks
    # everything you can find it with the rule of 3

    print( f'\n until the {event_date} will be: \n {years} years, {months} months, {weeks} weeks, and {diff.days} days \n')

if __name__ == "__main__":
    event()

