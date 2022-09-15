from time import sleep
import os

def run(): 
    
    x = int(input('\n Enter digit: \n '))
    y = x
    x = y 

    for i in range(x):
        x = x-1
        sleep(0.6)
        os.system('clear')
        print('Counting down: \n ', x)
        
    
    print('Start time: ', y)
    print('End time:   ', x)
    


if __name__ == '__main__':
    run()