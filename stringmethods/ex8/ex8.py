def findingnemo():
    word = 'Nemo'
    sentences = ['I am finding Nemo !', 'Nemo is me', 'I Nemo am', 'hello world']
    
    print(findingnemo)

    for i in sentences:
        if word in i:
            print(i + ' --> ' + 'I found Nemo at: ' + str(i.index(word)))
        else:
            print(i + ' --> ' + 'I cannot find Nemo :( ')
  
if __name__ =='__main__':
    findingnemo()