def run():
    #list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    menu = """
        January     February   March       April    May    June
        July        August     September   October
        November    December
        
        Input the name of month: 
        """
    option = str(input(menu))
    option.lower()
    if option == 'january' or 'march'or 'may' or 'july' or 'august' or 'october' or 'december':
        print('Number of days: 31 days')
    elif option == 'april'or 'june' or 'september' or 'november':
        print('Number of days: 30 days')
    else:
        Print('Number of days: 28 days')



if __name__ == '__main__':
    run()