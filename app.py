from models.user import User


credentials = []
user = None
def signUp():
    name= input("Enter your fullname :")
    email=input("Enter your email :")
    username= input("Enter your username :")
    password=input("Enter your password :")
    print("welcome "+name)

if __name__ ==  "__main__":
    if user is None:
        signUp()
