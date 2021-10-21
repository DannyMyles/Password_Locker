from models.user import User
from getpass import getpass

credentials = []
user = None
users =None
def signUp():
    name= input("Enter your fullname :")
    email=input("Enter your email :")
    username= input("Enter your username :")
    password=getpass("Enter your password :")
    print("welcome "+name)

def SignIn():
        username= input("Enter your username :")
        password=getpass("Enter your password :")

def createCredential():
    username= input("Enter your username :")
    domain= input("Enter your domain :")
    password=getpass("Enter your password :")

def createCredential():
    username= input("Enter your username :")
    domain= input("Enter your domain :")
    password=getpass("Enter your password :")


def Main():
    print("select an option:")
    print("1: Sign-in")
    print("2: Sign-up")
    print("3: create credentials")
    print("4: Retrive credentials ")
    action = input()

    if action==1:
        if user is None:
            SignIn()
        elif(action==2):
            signUp()
        


if __name__ ==  "__main__":
    while True:
        try:
            Main()

        except KeyboardInterrupt:
            print("Exit system")