def run():
    opt = str(input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius : "))
    opt = opt.upper()
    if opt == 'C':
        c = float(input("Input the value of temperature you'd like to convert  :"))
        f = (c * 9/5) + 32
        print('The temperature in Fahrenheit is ', f, ' degrees.')
    if opt == 'F':
        f= float(input("Input the value of temperature you'd like to convert  :"))
        c = (f - 32) * 5/9
        print('The temperature in Celsius is ', c, ' degrees.')
if __name__ == '__main__':
    run()