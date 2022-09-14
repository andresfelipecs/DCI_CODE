from time import sleep
import os

def run():
    

    for i in range(21):
        # bar= ':('
        # print('|', bar*21, '0 %' )
        bar = ':)'
        sleep(0.3)
        os.system('clear')
        print('|', bar*i, i*5, '%' )
        print('downloading nothing at all, please wait :D \n')
if __name__ == '__main__':
    run()