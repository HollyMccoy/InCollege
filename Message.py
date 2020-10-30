class Message:
    # class for messaging in the inbox
    def __init__(self,  # constructor
        currentUsername,
        recipient,
        message,isNew):
        self.isNew = isNew
        self.currentUsername = currentUsername
        self.recipient = recipient
        self.message = message
        

    def PrintMessagesToTxt(self):
         return ('\n**\n'+str(self.currentUsername) +'\n**\n'
        + self.recipient + '\n**\n'
        + self.message+ '\n**\n'+str(self.isNew)) 

    
        
    def Print(self):
        return ('\n******************\nFrom:'+str(self.currentUsername) +'\nTo:'
        + self.recipient + '\nMessage:\n'
        + self.message +'\n\n********************\n')

