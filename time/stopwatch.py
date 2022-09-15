import time
from time import sleep
import os

def run():
    ats = 562545215
    
    time_now = time.time()
    
    tim_diff = time_now - ats

    print('\n', time.ctime(), '\n')
    print('Current time in seconds: ', int(time_now), '\n')
    print(time.ctime(ats), '\n')
    print('Second date, time in seconds:', ats, '\n')

    sleep(0.6)
    print('From date:', time.ctime(ats), '  We have:', int(tim_diff), 'seconds of difference')
    minutes = tim_diff / 60 
    sleep(0.6)
    print('From date:', time.ctime(ats), '  We have:', int(minutes), 'minutes of difference')
    hours = tim_diff / 3600 
    sleep(0.6)
    print('From date:', time.ctime(ats), '  We have:', int(hours), 'hours of difference')
    days = tim_diff / 86400
    sleep(0.6)
    print('From date:', time.ctime(ats), '  We have:', int(days), 'days of difference \n ')

if __name__ == '__main__':
    run()