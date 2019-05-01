import os
import subprocess
import random
import string
import time

test_commands = ['2',
                'fuzz',
                'ADD "John Llanf" "123 Sesame Street" 92110 john@mail.com 800-555-5555', 
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
x = 0
y = 0
#Login
numLoginAttempts = random.randint(1, 255)
while x < numLoginAttempts:
    randNumArgs = random.randint(1, 90)
    ranStr = ''
    while y < randNumArgs:
        randStrLen = random.randint(1, 255)
        ranStr+= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randStrLen))
        ranStr+= " "
        y+=1
    test_commands.append("LOGIN "+ranStr)
    x+=1

x = 0
y = 0
#Get
numGetAttempts = random.randint(1, 255)
while x < numGetAttempts:
    randNumArgs = random.randint(1, 90)
    ranStr = ''
    while y < randNumArgs:
        randStrLen = random.randint(1, 255)
        ranStr+= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randStrLen))
        ranStr+= " "
        y+=1
    test_commands.append("GET "+ranStr)
    x+=1

x = 0
y = 0
#Add
numAddAttempts = random.randint(1, 255)
while x < numAddAttempts:
    randNumArgs = random.randint(1, 90)
    ranStr = ''
    while y < randNumArgs:
        randStrLen = random.randint(1, 255)
        ranStr+= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randStrLen))
        ranStr+= " "
        y+=1
    test_commands.append("ADD "+ranStr)
    x+=1

x = 0
y = 0
#Del
numDelAttempts = random.randint(1, 255)
while x < numDelAttempts:
    randNumArgs = random.randint(1, 90)
    ranStr = ''
    while y < randNumArgs:
        randStrLen = random.randint(1, 255)
        ranStr+= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(randStrLen))
        ranStr+= " "
        y+=1
    test_commands.append("DEL "+ranStr)
    x+=1

for test_command in test_commands:
    print(test_command)
    p.stdin.write(test_command.encode())
    p.stdin.write('\n'.encode())
    p.stdin.flush()
    

p.stdin.close()
for line in p.stdout.readlines():
    print(line.decode("utf-8"))
   
    
