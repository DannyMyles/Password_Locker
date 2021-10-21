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

if __name__ ==  "__main__":
    while True:
        try:
            if user is None:
                signUp()

        except KeyboardInterrupt:
            print()