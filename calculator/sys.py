import sys

def run():

    n1 = int(sys.argv[1]) 
    n2 = int(sys.argv[2]) 
    r1 = n1 + n2
    r2 = n1 - n2
    print('Sum result:', r1)
    print('Rest result: ', r2)

if __name__ == "__main__":
    run()