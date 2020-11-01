class Message:
    # class for messaging in the inbox
    def __init__(self,  # constructor
        currentUsername,
        recipient,
        message,isNew):
        self.currentUsername = currentUsername
        self.recipient = recipient
        self.message = message
        self.isNew = isNew

    '''
    # UNUSED
    # Non-asterisk version of appening inbox messages
    def PrintMessagesToTxt(self):
        return (str(self.currentUsername) + '\n'
        + self.recipient + '\n'
        + self.message + '\n'
        + str(self.isNew))
    '''

    #  Asterisk version of appending inbox messages
    def PrintMessagesToTxt(self):
        #return ('\n** + \n'+str(self.currentUsername) +'\n**\n'
        #+ self.recipient + '\n**\n'
        #+ self.message+ '\n**\n'+str(self.isNew))
        return ('**' + '\n'
            + str(self.currentUsername) + '\n'
            + '**' + '\n'
            + str(self.recipient) + '\n'
            + '**' + '\n'
            + str(self.message) + '\n'
            + '**' + '\n'
            + str(self.isNew) + '\n')


    def Print(self):
        return ('\n********************\nFrom: '+str(self.currentUsername) +'\nTo: '
        + self.recipient + '\nMessage:\n'
        + self.message +'\n\n********************\n')
