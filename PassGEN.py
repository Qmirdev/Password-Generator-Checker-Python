'''
Password Generator + Strength Checker
Developed by qmirdev
'''

import secrets
import string
import getpass
import logging
import datetime


print(" ")
print("Developed by")
print(" .d88b.  .88b  d88. d888888b d8888b.")
print(".8P  Y8. 88'YbdP`88   `88'   88  `8D")
print("88    88 88  88  88    88    88oobY'")
print("88    88 88  88  88    88    88`8b  ")
print("`8P  d8' 88  88  88   .88.   88 `88.")
print(" `Y88'Y8 YP  YP  YP Y888888P 88   YD")
print("                                 ^-^")
print(" ")

lengthx = input('Enter the length of the password: ')

# Set up logging
logging.basicConfig(filename='passwords.log', level=logging.DEBUG)

def create_pw(pw_length=int(lengthx)):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True

        logging.info(f"[{datetime.datetime.now()}] Generated password: {pwd}")

    return pwd


if __name__ == '__main__':
   print(" ")
   password = create_pw()
   print(password)
   print(" ")

   logging.info(password)


def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print(" ")
   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'* Remarks: {remarks}')

def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')

if __name__ == '__main__':
   print('===== Next step =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)

print(" ")
print("Have a good day <3")
print(" ")
logging.info('Exiting password generator')