import math
def run():
    print("Let's calculate the area of a circle O.O ")
    radius = float(input('Input the radius of the circle: '))
    area = math.pi * (radius**2)
    print('The area of the circle with radius', radius, ' is: ', area)


if __name__ == '__main__':
    run()