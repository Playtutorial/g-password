import random

chars = 'qwertyuiopasdfghjklzxcvbnm'

number = int(input("number of passwords: "))
lenght = int(input("number of characters in the password: "))

for x in range(number):
    password = ''
    
    for i in range(lenght):
        password += random.choice(chars)
        
    print(password)