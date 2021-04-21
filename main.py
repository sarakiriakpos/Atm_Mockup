name = input('What is your name? \n')
currentBalance = 50000
allowedUsers = ['Akpos', 'Seyi', 'Peace']
allowedPassword = ['passwordAkpos', 'passwordSeyi', 'passwordPeace']

if(name in allowedUsers):
    password = input('Your password \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        import datetime
        datetime.datetime.now()
        print(datetime.datetime.now())
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if(selectedOption == 1):
            input('How much would you like to withdraw:')
            print('take your cash')

        elif(selectedOption == 2):
            int(input('How much would you like to deposit:'))
            print('your current balance is %s' % currentBalance)

        elif(selectedOption == 3):
            input('What issue will you like to report?: \n')
            print('Thank you for contacting us')

        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password incorrect, please try agin.')

else:
    print('Name not found, please try again.')