import time
import os

def run():
    
    time_now = time.ctime()
    another_time = time.ctime(562545215)
    print(time_now, '\n')
    print(another_time, '\n')
    tim_diff = 562545215 
    print('From date:', another_time, '  We have:', tim_diff, 'seconds of difference')
    minutes = tim_diff / 60 
    print('From date:', another_time, '  We have:', minutes, 'minutes of difference')
    hours = tim_diff / 3600 
    print('From date:', another_time, '  We have:', hours, 'hours of difference')
    days = tim_diff / 86400
    print('From date:', another_time, '  We have:', days, 'hours of difference')

if __name__ == '__main__':
    run()