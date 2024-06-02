# CODE FOR MAKING SIMPLE PASSWORD BASE ON FEW COMMANDS #.

import random as rm 
import string as st

print('WELLCOME TO SIMPLE PASSSWORD MAKER'.center(100))
name = input('Enter your good name :'.center(10))
choice = input(f"wellcome {name} for making passwaord by randomly type 'random' otherwise type 'name 'for making by name :".center(10))
lenght1 = int(input('enter the lenght for password :'.center(10)))
def genrate_password_from_name(name,lenght):
    char = name + st.digits + name
    password =''.join(rm.choice(char) for _ in range(lenght))
    return password
def genrate_random_password(lenght):
    characters = st.ascii_letters+st.digits+st.punctuation
    password = ''.join(rm.choice(characters) for _ in range(lenght))
    return password

if choice.lower() == "random":
    type =int(input('enter the numbers of time you want passward : '.center(10)))
    for x in range(type):
        genrate_password = genrate_random_password(lenght1)
        print("Genrated_password is :".center(10), genrate_password)
        
else:
    password = genrate_password_from_name(name,lenght1)
    print('Genrated_password is :'.center(10),password)
print(f'Thank you {name} for visit '.center(50).upper())    
