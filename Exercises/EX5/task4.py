import math
def run():
    print("Let's calculate the area of a circle O.O ")
    radius = float(input('Input the radius of the circle: '))
    #radius = round(radius, 2)
    #area = math.pi * (radius **2)
    area = round(pi * radius**2, 2)
    print('The area of the circle with radius', radius, 'is: ', round(area, 2))


if __name__ == '__main__':
    run()