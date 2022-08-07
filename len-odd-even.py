def run():
    string1 = '"hello world"'
    string2 = '"hello planet"'
    string3 = '""'

    len1 = len(string1)
    len2 = len(string2)
    len3 = len(string3)
    
    if  len1 % 2 != 0:
        print(string1 + '     -->    ' + '"odd"')
    
    if len2 % 2 == 0:
        print(string2 + '    -->    ' + '"even"')
    
    if len3 % 2 == 0:
        print(string3 + '                -->    ' + '"even"')

#  "hello world"     -->    "odd"  
#  "hello planet"    -->    "even"  
#  ""                -->    "even"  

if __name__ == '__main__':
    run()