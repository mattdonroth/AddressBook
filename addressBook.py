import argparse
import re

class address_book:
    def __init__(self):
        self.address_book = {}

    def isEmail(self,number):
        variable = 1

        regex = "[^@]+@[^@]+\.[^@]+"
        if re.search(regex, number) and len(number) < 320:
            print("valid")
            return (True)

        else:
            print("not valid")
            return False

    def isAddress(self,number):
        if len(number) < 60:
            print("valid")
            return (True)

        else:
            print("not valid")
            return False
    def isZipCode(self,number):
        number = number.replace("-", "")
        number = number.replace(" ", "")

        if len(number) < 16 and number.isdigit() and len(number) > 4:
            print("valid")
            return (True)

        else:
            print("not valid")
            return False
    def isPhoneNumber(self,number):
        variable = 1

        regex = "\w{3}-\w{3}-\w{4}"

        if re.search(regex, number):
            print("valid number")
            return True
        else:
            number = number.replace("-", "")
            number = number.replace("(", "")
            number = number.replace(")", "")
            number = number.replace(" ", "")
            if (len(number) == 10) and number.isdigit():
                print("valid")
                return True
            else:
                print("invalid")
                return False

    def isName(self,number):
        if len(number) < 60:
            print("valid")
            return (True)

        else:
            print("not valid")
            return False

    def record_add(self, Name, address):
        if len(self.address_book) > 5:
            return None
        else:
            self.address_book[Name] = address
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
            return out
        except:
            return None

    def old_shell(self):
        flag = True
        while flag:
            seel = input(
                "Please Select An Option:\n1. Get a Record\n2. Add a Record\n3. Delete a Record\n4. Exit\n")
            try:
                sel = int(seel)
            except:
                print("Please enter an integer.")
                sel = None
            if sel > 5:
                print("Please enter a valid selection")
            elif sel == 1:
                arg = input("Please enter a name to lookup:")
                out = self.record_get(arg)
                if out == None:
                    print("Record Not Found")
                else:
                    print(out)
            elif sel == 2:
                arg1 = input("Please enter the Name to add:")
                arg2 = input("Please enter the Address to add:")
                if type(arg1) != str or type(arg2) != str:
                    print("Please enter a valid input")
                else:
                    out = self.record_add(arg1, arg2)
                    if out == None:
                        print("Record not added, address book is full")
                    elif out == True:
                        print("Record added")
            elif sel == 3:
                arg1 = input("Please enter the Name to remove:")
                out = self.record_del(arg1)
                if out == True:
                    print("Record Removed")
                elif out == False:
                    print("Record not found.")
            elif sel == 4:
                flag = False
                print("Thanks for using the most advanced address book system in the world. Have a nice day!")


if __name__ == "__main__":

    this = address_book()
    this.old_shell()

    parser = argparse.ArgumentParser()
    parser.add_argument("-ADD", help="Add a user to the Address Book")
    parser.add_argument("-DEL", help="Delete a user from the Address Book")
    parser.add_argument("-GET", help="Get a user from the Address Book")
    parser.add_argument("-UPDATE", help="Update an existing user in the Address Book")
    parser.add_argument("-LIST", help="List all users in the Address Book")
    args = parser.parse_args()
    print(args)
