def normalize():
    string = input(str('Enter string: '))
    if string.isupper():
        string = string.lower() + string.join('!')
        string = string.capitalize() 
        print(string)
    else:
        string = string.capitalize()
        print(string)



if __name__ == '__main__':
    normalize()