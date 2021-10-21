from _typeshed import Self


class User:
    def _init_(self,name, username,email):
        self.name = name
        self.email = email
        self.username =username

class Users:
   def signIn(self,username,password):
       print(username)
