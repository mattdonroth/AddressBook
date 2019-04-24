import getpass
import addressBook
logins = {}

class account:
    def __init__(self, username, password, addressBook):
        self.addressBook = addressBook
        self.username = username
        self.password = password



def create_account():
    print('Enter username: ')
    username = input()
    if username in logins.keys():
        print('Username already exists. Please enter another one: ')
        username = input()
    
    print('Enter password: ')
    try:
        password = getpass.getpass()
    except Exception as error:
        print(error)
    else:
        print('Password entered: ' + password)

    logins[username] = password
    print("Account successfully created")
    return account(username, password, addressBook.address_book())



