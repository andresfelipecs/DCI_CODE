from datetime import datetime, timedelta, date


def run():

    ## Python datetime module
    # create a variable that stores the current time
    today = datetime.now()

    # print out current year
    # print(today.year)
    year = today.strftime("%Y")
    print(year)

    # Print the weekday of the week
    weekday = today.strftime('%A')
    print(weekday)

    # Convert a string into a datetime object
    date = 'January 1, 2005'
    con = datetime.strptime(date, "%B %d, %Y")
    print(con)




if __name__ == '__main__':
    run()
