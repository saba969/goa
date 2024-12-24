print("registration")

name = input("enter your name: ")
password = input("enter your passward: ")




print("login: ")

log_name = input("enter your name: ")
log_passward = input("enter your passward: ")


while log_name != name or log_passward != password:
    print("inccorect name or password, please try again")

    log_name = input("please enter correct name: ")
    log_password = input("please enter correct passworf: ")


print("welcome")