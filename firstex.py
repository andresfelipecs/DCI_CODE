def run():
    emails = ["123whatever@gmail.com","456idontcare@gmail.com","789istilldontmind@hotmail.de","forrealbruvwhatever@gmx.de"]
    
    name_list = []
    email_list = []

    for username in emails:
        both = username.split('@')
        username_name = both[0]
        name_list.append(username_name)
        username_email = both[1]
        email_list.append(username_email)

    print('usernames: '+ str(name_list)) 
    print('emails: ' + str (email_list)
    )



    #username1 = emails[0]
    #both = username1.split('@')
    #username1_name = both[0]
    #username1_email = both[1]


    #atpos1 = username1.find('@')
    #username1_name = username1[:atpos1]
    #username1_email = username1[atpos1+1:]

    #username1_name = username1[0:11]
    #username1_email = username1[-9:]
    #print('Username 1: ' + username1_name)
    #print('Email provider 1 : ' + username1_email)

    #username2 = emails[1]
    #atpos2 = username2.find('@')
    #username2_name = username2[:atpos2]
    #username2_email = username2[atpos2+1:]

    #username2_name = username2[0:12]
    #username2_email = username2[-9:]
    #print('Username 2: ' + username2_name)
    #print('Email provider 2 : ' + username2_email)

    #username3 = emails[2]
    #atpos3 = username3.find('@')
    #username3_name = username3[:atpos3]
    #username3_email = username3[atpos3+1:]

    #username3_name = username3[0:17]
    #username3_email = username3[-10:]
    #print('Username 3: ' + username3_name)
    #print('Email provider 3 : ' + username3_email)

    #username4 = emails[3]
    #atpos4 = username4.find('@')
    #username4_name = username4[:atpos4]
    #username4_email = username4[atpos4+1:]

    #username4_name = username4[0:19]
    #username4_email = username4[-6:]
    #print('Username 4: ' + username4_name)
    #print('Email provider 4 : ' + username4_email)

    #usernames = [username1_name,username2_name, username3_name, username4_name ]
    #email_provider = [username1_email, username2_email, username3_email, username4_email]
    #print('usernames: ' + str(usernames))
    #print('emails: ' + str(email_provider))


if __name__ == '__main__':
    run()



# please fill the two lists with the data from the "emails" list. Use string slicing and methods for extracting what you need
#example:
#  test@mail.com
# usernames = ["test"]
# email_provider = ["mail.com"]