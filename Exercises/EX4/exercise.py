# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#TASK1

def run():
    counter = 0
    while counter < 2:
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        
        if number1 != number2:
            print('Number are not equal')
        else:
            print('Numbers are equal')
        if number2 > number1:
            print('Second number is greater than first number')
        else:
            print('Second number is equal and/or smaller than first number')
        if number2 > number1 or number2 == number1:
            print('Second number is greater than or equal to first number')
        else:
            print('Second number is smaller than or not equal to first number')
        if number1 >= 5000 and number2 >= 5000:

            print('Both numbers are big!')
        else:
            print('Both numbers are not big :(')
        #counter += 1
        #big_numbers = True
        #for i in range(2):
            # for value in big_numbers:(its not possible to iterate a Boolean)
        if counter == 0:
        #for value in [1,2]:
            big_numbers = True   
            #if value == 1: 
            #if big_numbers == True:
            print('big_numbers is set to ', big_numbers)
        else:
            big_numbers = False
            print('big_numbers is set to ', big_numbers)
            #continue
            #big_numbers = False
            #for value in big_numbers:
            #    if big_numbers == False:
            #       print('big_numbers is set to ', big_numbers)

            
        counter += 1
        


if __name__ == '__main__':
    run()