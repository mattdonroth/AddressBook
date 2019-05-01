import getpass
import addressBook
import db
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

logins = {}

class account:
    def __init__(self, username, password, addressBook):
        self.addressBook = addressBook
        self.username = username
        self.addressBook.username = username
        self.password = password

def login(username, password):
    if(db.check(username, password)):
        return True
    else:
        return False
        


def loadin_account(username, password):
    contacts = db.show(username)
    data = {}
    for contact in contacts:
        data[contact[0]] = contact[1:]
    return account(username, password, addressBook.address_book(data))

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
    return account(username, password, addressBook.address_book({}))



