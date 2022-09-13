import re


def make_happy():


    list = ['My current mood: :(', 'I was hungry 8(', 'print("x(")', 'hola ;(']
        
    pattern = '\:\(|8\(|x\(|;\('
    pattern2 = '\('

    for i in list:

        faces = re.findall(pattern, i)
        
        for face in faces:
            replacement = re.sub(pattern2, ')', face)
        
        replacement2 = re.sub(pattern, replacement, i )

        print('make_happy (', i, ')    --> ', replacement2)
    
            
if __name__ == '__main__':
    make_happy()