


x = int(input("First number: ")) # bug
y = int(input("Second number: ")) #bug

if x %y == 0: # 2 bugs
    print("First number is divisible by second number, result =", x / y) #bug
elif y %x == 0: # 2 bugs
    print("Second number is divisible by first number, result =", y // x) #bug
else:
    print("Numbers are non-divisable!")
    