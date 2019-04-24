import argparse
import re
import sys

class address_book:
    def __init__(self):
        self.address_book = {}

    def isEmail(self,number):
        regex = "[^@]+@[^@]+\.[^@]+"
        if re.search(regex, number) and len(number) < 320:
            return (True)

        else:
            print("invalid email")
            return False

    def isAddress(self,number):
        if len(number) < 60:
            return (True)

        else:
            print("invalid address")
            return False
    def isZipCode(self,number):
        number = number.replace("-", "")
        number = number.replace(" ", "")

        if len(number) < 16 and number.isdigit() and len(number) > 4:
            return (True)

        else:
            print("invalid zipcode")
            return False
    def isPhoneNumber(self,number):
        regex = "\w{3}-\w{3}-\w{4}"

        if re.search(regex, number):
            return True
        else:
            number = number.replace("-", "")
            number = number.replace("(", "")
            number = number.replace(")", "")
            number = number.replace(" ", "")
            if (len(number) == 10) and number.isdigit():
                return True
            else:
                print("invalid phone number")
                return False

    def isName(self,number):
        if len(number) < 60:
            return (True)

        else:
            print("invalid name")
            return False

    def addCheck(self, name, address, zip, email, number):
        if self.isName(name) and self.isAddress(address) and self.isZipCode(zip) and self.isEmail(email) and self.isPhoneNumber(number):
            return True
        else:
            return False

    def record_add(self, name, address, zip, email, number):
        if len(self.address_book) > 5:
            return None
        elif name in self.address_book.keys():
            print("Name already exists")
        else:
            self.address_book[name] = address, zip, email, number
            return True

    def record_del(self, Name):
        try:
            del self.address_book[Name]
            return True
        except:
            return False

    def record_get(self, Name):
        try:
            out = self.address_book[Name]
            print("Name: " + str(Name) +  "\nAddress: " + str(out[0]) + " " + str(out[1]) + "\nEmail: " + str(out[2]) + "\nPhone: " + str(out[3]))
        except:
            print("Uh oh")
    
    def new_shell(self):
        flag = True
        while(flag):
            seel = input()
            if len(seel) == 0:
                print("Please try again")
                seel = None
            elif seel.split(' ')[0] == 'ADD':
                try:
                    name = seel.split('"')[1]
                    address = seel.split('"')[3] 
                    rest = seel.split('"')[4]
                    zip = rest.split(" ")[1]
                    email = rest.split(" ")[2]
                    phone = ''.join(rest.split(" ")[3:])
                    if self.addCheck(name, address, zip, email, phone):
                        self.record_add(name, address, zip, email, phone)
                    else:
                        print('ADD command rejected\nInput Outline: ADD "Name" "Address" Zipcode Email Phone\nEg: ADD "John" "123 Main" 92110 john@mail.com 9165155115')
                except:
                    print('Invalid command try again\nInput Outline: ADD "Name" "Address" Zipcode Email Phone\nEg: ADD "John" "123 Main" 92110 john@mail.com 9165155115')
                    seel = None
                seel = None
            elif seel.split(' ')[0] == 'DEL':
                try:
                    name = seel.split('"')[1]
                    if self.isName(name) and name in self.address_book.keys():
                        self.record_del(name)
                        print(self.address_book)
                    else:
                        print("DEL command rejected, name not found")
                        seel = None
                except:
                    print("Invalid command try again")
                    seel = None
            elif seel.split(' ')[0] == 'GET':
                try:
                    name = seel.split('"')[1]
                    if self.isName(name) and name in self.address_book.keys():
                        self.record_get(name)
                    else:
                        print("GET command rejected, name not found")
                        seel = None
                except:
                    print("Invalid command try again")
                    seel = None
            elif seel.split(' ')[0] == 'UPDATE':
                name = seel.split('"')[1]
            elif seel.split(' ')[0] == 'LIST':
                for index, name in enumerate(self.address_book.keys()):
                    print("Address Book Record Number " + str(index+1) + ":")
                    self.record_get(name)
            elif seel.split(' ')[0] == "EXIT":
                print("GOODBYE")
                sys.exit()
            else:
                print("Invalid command try again")
                seel = None






if __name__ == "__main__":

    this = address_book()
    this.new_shell()

    parser = argparse.ArgumentParser()
    parser.add_argument("-ADD", help="Add a user to the Address Book")
    parser.add_argument("-DEL", help="Delete a user from the Address Book")
    parser.add_argument("-GET", help="Get a user from the Address Book")
    parser.add_argument("-UPDATE", help="Update an existing user in the Address Book")
    parser.add_argument("-LIST", help="List all users in the Address Book")
    args = parser.parse_args()
    print(args)
