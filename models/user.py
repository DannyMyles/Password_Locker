
allUsers = []


class User:
    def __init__(self,name, username,email,password):
        self.name = name
        self.email = email
        self.username =username
        self.password =password

class Users:
   def signIn(self,username,password):
       for user in allUsers:
           if(user.username == username and user.password == password):
               return user

       return None

   def signUp(self,user,password):
        print(user)
        for usr in allUsers :
            if user.email==usr.email :
                return "emial already in use"
            if user.username==usr.username :
                return "username already in use"
        newUser = User(user.name, user.username, user.email, password)
        allUsers.append(newUser)

        return "User created successfully wecome"+newUser.name
