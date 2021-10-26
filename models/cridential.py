class Credential:
     def __init__(self,user,username,domain,password):
         self.user =user
         self.username = username
         self. domain =password

class Credentials:
    def __init__(self) -> None:
        pass

    def Save(self,credential):
        print(credential)

    def Get(self,credential):
        print(credential)

    def Delete(self,credential):
        print(credential)


