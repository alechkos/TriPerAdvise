import os
import firebase as fb

# Function for authentication of registered user
def enter():
    mail = input("Enter your mail: ")
    password = input("Enter your password:")
    fb.auth.sign_in_with_email_and_password(mail, password)
# Function for registration of user
def registration():
    mail = input("Enter your mail: ")
    password = input("Enter your password:")
    fb.auth.create_user_with_email_and_password(mail, password)

# Menu
log, sign = "Sign in", "Sign up"
print("{:*^20s}".format(" MENU "))
print("{0: ^10s} {1: ^10s}".format(log, sign))

inp_user = input("Enter your choice: ").lower()
while inp_user != log.lower() and inp_user != sign.lower():
    print("{:*^20s}".format(" MENU "))
    print("{0: ^10s} {1: ^10s}".format(log, sign))
    inp_user = input("Enter your choice: ").lower()

os.system('cls')
if inp_user == log.lower():
    print("{: ^60}".format(log))
    enter()
else:
    print("{: ^60}".format(sign))
    registration()

