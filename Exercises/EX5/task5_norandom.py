def run():
    #random_number = random.randint(1, 9)
    lon = [9,5,1,2,8,10,4,3,7,9,6]
    random_number = lon[8]
    number = int(input("Guess a number between 1 and 10 until you get it right : "))
    if number > 10 or number <= 0:
        print('Please enter a number from 1 to 10')
    else:   
        while number != random_number:
            if number < random_number or number > random_number:
                number = int(input("Guess a number between 1 and 10 until you get it right : "))
            
        print("Well guessed !")


if __name__ == '__main__':
    run()