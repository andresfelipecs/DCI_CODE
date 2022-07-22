def run():
    text = "Berlin is surrounded by the stat of Brandenburg and contiguous with Potsdam, Brandenburgs's capital"
    if text.find('capital') != -1:
        text3 = text.index('capital')
        print('capital: ' + str(text3))
    else:
        print('The word is not in the text')

if __name__ == '__main__':
    run()