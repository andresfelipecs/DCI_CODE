import random

def run():
    random_number = random.randint(1, 9)
    number = int(input("Guess a number from 1 to 9 :"))
    if number > 9 or number <= 0:
        print('Please enter a number from 1 to 9')
    else:   
        while number != random_number:
            if number < random_number:
                print("Enter a bigger number ")
            else:
                print("Enter a smaller number ")   
            number = int(input("Enter a different number: "))
        
        print("You guessed right,",number,  "that is the number !")


if __name__ == '__main__':
    run()