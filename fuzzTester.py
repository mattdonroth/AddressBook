import os

test_commands = ['-ADD "John Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch" "123 Sesame Street" 92110 john@mail.com 800-555-5555']

for test_command in test_commands:
    os.system('python addressBook.py ' + test_command)