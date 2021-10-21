from models.user import User
from getpass import getpass

credentials = []
user = None
def signUp():
    name= input("Enter your fullname :")
    email=input("Enter your email :")
    username= input("Enter your username :")
    password=getpass("Enter your password :")
    print("welcome "+name)

def Main():
    print("select an option:")
    print("1: Sign-in")
    print("2: Sign-up")
    print("3: create credentials")
    print("4: Retrive credentials ")
    action = input()


if __name__ ==  "__main__":
    while True:
        try:
            if user is None:
                signUp()

        except KeyboardInterrupt:
            print("Exit system")