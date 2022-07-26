def run():
    text = 'Berlin is a world city of culture, politics, media and science.'
    text2 = text[0:63:62]
    text3 = text[0] + ' ' + text[-1]
    print(text2)
    print(text3)

if __name__ == '__main__':
    run()