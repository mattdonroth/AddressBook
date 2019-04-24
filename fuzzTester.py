import os
import subprocess

test_commands = ['ADD "John Llanf" "123 Sesame Street" 92110 john@mail.com 800-555-5555', 'LIST']



p = subprocess.Popen("python addressBook.py", shell=True, stderr=subprocess.PIPE, 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
for test_command in test_commands:
    p.stdin.write(test_command.encode())
    p.stdin.write('\n'.encode())
    p.stdin.flush()

p.stdin.close()
for line in p.stdout.readlines():
    print(line.decode("utf-8"))
   
    
