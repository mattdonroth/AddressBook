class address_book:
    def __init__(self):
        self.address_book = {}

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


if __name__ == "__main__":
    this = address_book()
    flag = True
    while flag:
        seel = raw_input("Please Select An Option:\n1. Get a Record\n2. Add a Record\n3. Delete a Record\n4. Exit\n")
        try:
            sel = int(seel)
        except:
            print("Please enter an integer.")
            sel = None
        if sel > 5:
            print("Please enter a valid selection")
        elif sel == 1:
            arg = raw_input("Please enter a name to lookup:")
            out = this.record_get(arg)
            if out == None:
                print("Record Not Found")
            else:
                print(out)
        elif sel == 2:
            arg1 = raw_input("Please enter the Name to add:")
            arg2 = raw_input("Please enter the Address to add:")
            if type(arg1) != str or type(arg2) != str:
                print("Please enter a valid input")
            else:
                out = this.record_add(arg1, arg2)
                if out == None:
                    print("Record not added, address book is full")
                elif out == True:
                    print("Record added")
        elif sel == 3:
            arg1 = raw_input("Please enter the Name to remove:")
            out = this.record_del(arg1)
            if out == True:
                print("Record Removed")
            elif out == False:
                print("Record not found.")
        elif sel == 4:
            flag = False
            print("Thanks for using the most advanced address book system in the world. Have a nice day!")

# Assets = The data contained within the address book.
# Possible Harm = Data being obtained outside of the record_get function.
#                 Breaking the menu system.
# Policy = Only allow data to be called through the record_* functions.
#          Catch edge cases in user input in the menu system.