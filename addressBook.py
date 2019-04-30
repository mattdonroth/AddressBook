import re
import sys
import login
import db


class address_book:
    def __init__(self, data):
        self.address_book = data
        self.username = ''

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
            db.add(name, address, zip, email, number, self.username)
            print("Successfully added " + name)
            return True

    def record_del(self, Name):
        try:
            del self.address_book[Name]
            db.delete(Name, self.username)
            return True
        except:
            return False

    def record_get(self, Name):
        try:
            out = self.address_book[Name]
            print("Name: " + str(Name) +  "\nAddress: " + str(out[0]) + " " + str(out[1]) + "\nEmail: " + str(out[2]) + "\nPhone: " + str(out[3]))
            return out
        except:
            print("Uh oh")
            return None

    def update_record(self, record, number, old):
        if number == '1':
            print("Enter new name:")
            name = input()
            if self.isName(name):
                self.address_book[name] = self.address_book.pop(old)
                print("Updated name to " + name)
            else:
                name = None
        elif number == '2':
            print("Enter new zipcode:")
            zip = input()
            if self.isZipCode(zip):
                self.address_book[old] = (record[0], zip, record[2], record[3])
                print("Updated zip code to " + zip)
            else:
                print("Enter new zipcode:")
                zip = None
        elif number == '3':
            print("Enter new address:")
            address = input()
            if self.isAddress(address):
                self.address_book[old] = (address, record[1], record[2], record[3])
                print("Updated address to " + address)
            else:
                print("Enter new address:")
                address = None
        elif number == '4':
            print("Enter new email:")
            email = input()
            if self.isEmail(email):
                self.address_book[old] = (record[0], record[1], email, record[3])
                print("Updated email to " + email)
            else:
                print("Enter new email:")
                email = None
        elif number == '5':
            print("Enter new phone number:")
            phone = input()
            if self.isPhoneNumber(phone):
                self.address_book[old] = (record[0], record[1], record[2], phone)
                print("Updated phone number to " + phone)
            else:
                print("Enter new phone number:")
                phone = None
        else:
            print("Try again")
            number = input()
            self.update_record(record, number, old)     

        

            


    def new_shell(self):
        print("Please enter a desired command:")
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
                        print("Successfully deleted " + name)
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
                try:
                    name = seel.split('"')[1]
                    if self.isName(name) and name in self.address_book.keys():
                        print('1: Update Name\n2. Update Zip code\n3: Update Address\n4: Update Email\n5: Update Phone Number')
                        seel = input()
                        self.update_record(self.address_book[name], seel, name)
                    else:
                        print("GET command rejected, name not found")
                        seel = None
                except Exception as e:
                    print("Invalid command try again", e)
                    seel = None
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


def login_prompt():
    print("Welcome to Address Book Program: Please Login or Create an Account")
    print("Enter login command")
    choice = input()
    split = choice.split(' ')
    if split[0] == 'LOGIN':
        return login.loadin_account(split[1], split[2])
    






if __name__ == "__main__":

    account = login_prompt()
    account.addressBook.new_shell()

