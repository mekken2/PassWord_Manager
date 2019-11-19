#! python3
# A PassWord Manager developed as Python project

import sys
import pyperclip

PASSWORDS = {'email1': 'hdsfjfaj13%^',
             'facebook': 'skdfj534632#$',
             'email2': 's354rwercx'}

if len(sys.argv) < 2:
    print('Usage: Python PassWord_Manager.py [account] - copy account password')
    sys.exit()

#first command line argument is the account name
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    create = input('Do you want to create an account with this name(y/n)?:')
    if create == 'y' or create == 'Y':
        create_pass = input('Enter the PassWord for the account: ')
        PASSWORDS[create] = create_pass
    else:
        sys.exit()