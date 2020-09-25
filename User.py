#User object class
class User:
    def __init__(self, username, password, firstname, lastname):     #constructor
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def CheckLogin(self, inputUser, inputPass):    #check login returns true if input is a valid account login, false if it is not a valid account
        if (self.username == inputUser):
            if (self.password == inputPass):
                return True
        return False

    def Print(self):
        return (self.username + ' '
        + self.password + ' '
        + self.firstname + ' '
        + self.lastname)
