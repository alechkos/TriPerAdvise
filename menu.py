import os

def Input_Info(name, mail, phone):
    name = input("Enter your name: ")
    mail = input("Enter your e-mail: ")
    phone = input("Enter your phone: ")


log, sign = "Log in", "Sign up"
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
    u_name = input("Enter your name: ")
    password = input("Enter your password: ")
else:
    print("{: ^60}".format(sign))
    name, mail, phone = None, None, None
    Input_Info(name, mail, phone)


