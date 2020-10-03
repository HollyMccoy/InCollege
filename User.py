#User object class
class User:
    def __init__(self,  # constructor
        username,
        password,
        firstname,
        lastname,
        emailAlerts,
        textAlerts,
        targetedAdvertising,
        language):

        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.emailAlerts = emailAlerts
        self.textAlerts = textAlerts
        self.targetedAdvertising = targetedAdvertising
        self.language = language


    def CheckLogin(self, inputUser, inputPass):    #check login returns true if input is a valid account login, false if it is not a valid account
        if (self.username == inputUser):
            if (self.password == inputPass):
                return True
        return False

    def Print(self):
        return (self.username + ' '
        + self.password + ' '
        + self.firstname + ' '
        + self.lastname + ' '
        + str(self.emailAlerts) + ' '
        + str(self.textAlerts) + ' '
        + str(self.targetedAdvertising) + ' '
        + self.language)
