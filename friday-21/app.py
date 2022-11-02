## This file we greet a user
## we ask them for what they want to do?
## - if they choose to add, we ask questions like what do they want to add
## - if they choose to subtract, we ask them for input

import add
import subtraction

if __name__ == '__main__':
    user = input("Which math operation do you want to achive ? Choose 1 for Add. Choose 2 for Subtraction \n")
    a = int(input("A: "))
    b = int(input("B: "))
    if user == "1":
        print(f"Your total is: {add.add(a, b)}")
    elif user == "2":
        print(f"Your total is: {subtraction.subtraction(a, b)}")