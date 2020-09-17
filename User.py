#User object class
class User:
    def __innit__ ( self, username = "NULL",  password = "NULL"):     #constructor
        self.username = username
        self.password = password


    def CheckLogin (self, inputUser, inputPass):    #check login returns true if input is a valid account login, false if it is not a valid account
        if (self.username == inputUser):
            if (self.password == inputPass):
                return true
        return false

