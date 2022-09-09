import sys
import getopt

def full_name():
	first_name = None
	last_name = None

	argv = sys.argv[1:]

	opts, args = getopt.getopt(argv,"f:l:")

	for opt, arg in opts:
		if opt in ['-f', '--first_name']:
			first_name = arg
		elif opt in ['-l', '--last_name']:
			last_name = arg


	print( first_name +" " + last_name)
	
if __name__ == '__main__':
    full_name()
 