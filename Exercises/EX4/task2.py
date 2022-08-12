def run():
    list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    #menu = """
        #January     February   March       April    May    June
        #July        August     September   October
        #November    December
        
        #Input the name of month: """
    #option = str(input(menu))
    print('List of months: ', list)
    #for i in list:
    #    list = i.lower()
    #months = list.split()
    #months.lower()
    option = str(input('Input the name of month: '))
    option.lower()
    if option == 'january' or option == 'march'or option == 'may' or option == 'july' or option == 'august' or option == 'october' or option == 'december':
        print('Number of days: 31 days')
    elif option == 'april'or option == 'june' or option == 'september' or  option == 'november':
        print('Number of days: 30 days')
    elif option == 'february':
        print('Number of days: 28 days')
    else:
        print('Enter a correct value')



if __name__ == '__main__':
    run()