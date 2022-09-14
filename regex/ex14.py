import re


def run():

    list = ['0023.07623070', 'hello world', '01230']

    pattern = '\A0+'
    
    pattern2 = '0+\Z'

    final_list = []

    print('\n')

    for i in list:

        if len(i) > 5:
        
            replacement = re.sub(pattern, '', i)

            replacement2 = re.sub(pattern2, '', replacement)
        
            final_list.append(replacement2)

        else:
            
            replacement3 = re.sub(pattern, '', i)

            final_list.append(replacement3)

    #print(final_list)

    print('"0023.07623070"   -->  ', final_list[0] )
    print('"hello world"     -->  ', final_list[1] )
    print('"01230"           -->  ', final_list[2] )
    print('\n')

if __name__ == '__main__':
    run()