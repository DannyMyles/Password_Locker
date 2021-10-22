from os import path
from models.user import User, Users
from getpass import getpass

credentials = []
user = None
users =None
def signUp():
    name= input("Enter your fullname :")
    email=input("Enter your email :")
    username= input("Enter your username :")
    password=getpass("Enter your password :")
    appUser=User(name,username,email,password)
    appUsers = Users()
    response= appUsers.signUp(appUsers)
    print(response)

def SignIn():
        username= input("Enter your username :")
        password=getpass("Enter your password :")
        appUsers= Users()
        user =appUsers.signIn(username,password)
        if user is None:
            print("User name or password invalic")
        else:
            print("welcome " +user.name+"you can now manage your password")


def createCredential():
    username= input("Enter your username :")
    domain= input("Enter your domain :")
    password=getpass("Enter your password :")

def retriveCredential():
    domain= input("Enter your domain :")


def Main():
    print("select an option:")
    print("1: Sign-in")
    print("2: Sign-up")
    print("3: create credentials")
    print("4: Retrive credentials ")
    action = input()

    print("(action) "+(action))

    if int(action)==1:
        SignIn()

    elif int(action)==2:
        signUp()

    elif int(action)==3:
        createCredential()

    elif int(action)==4:
        retriveCredential()


if __name__ ==  "__main__":
    while True:
        try:
            Main()

        except KeyboardInterrupt:
            print("Exit system")
