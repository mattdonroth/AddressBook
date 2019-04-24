import os
import subprocess

test_commands = ['ADD "John Llanf" "123 Sesame Street" 92110 john@mail.com 800-555-5555', 
                 'ADD "123" "John Llanf" john@mail.com 92110 800-555-5555',
                 'ADD john@mail.com "John Llanf" 800-55-5555 92110',
                 'ADD , fjdskal, fdsa',
                 'ADD "John Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch" "123 Sesame Street" 92110 john@mail.com 800-555-5555',
                 'ADD "John" "123 Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch" 92110 john@mail.com 800-555-5555',
                 'ADD "John" "123 Sesame Streeet" 921111111111111111110 john@mail.com 800-555-5555',
                 'LIST',
                 'LIST 123',
                 'LIST fdsab',
                 'LIST fdsab 134',
                 'UPDATE',
                 'UPDATE name',
                 'UPDATE 1',
                 'UPDATE 2',
                 'UPDATE 3',
                 'UPDATE 4',
                 'UPDATE A',
                 'UPDATE ,,,,',
                 'DEL "John Llanf"',
                 'DEL "123 Sesame Street',
                 'DEL 92110',
                 'DEL john@mail.com',
                 'GET "123 Sesame Street"',
                 'GET "John Llanf"',
                 'GET 800-555-5555',
                 'GET ,,,',
                 'GET john@mail.com']



p = subprocess.Popen("python addressBook.py", shell=True, stderr=subprocess.PIPE, 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
for test_command in test_commands:
    p.stdin.write(test_command.encode())
    p.stdin.write('\n'.encode())
    p.stdin.flush()

p.stdin.close()
for line in p.stdout.readlines():
    print(line.decode("utf-8"))
   
    
