import globals
from Message import Message


class Inbox:
    def __init__(self):
        self.inboxAllAccounts=[]


    def SendMessage(self,currentUser,recipient,text):
        """Append a message to memory and onto file."""
        self.inboxAllAccounts.append(Message(str(currentUser),recipient,text,True))
        with open("Messages.txt", "a+") as file1:
            file1.write(self.inboxAllAccounts[len(self.inboxAllAccounts)-1].PrintMessagesToTxt())
        print("\nMessage sent!\n")
        return


    def UpdateMessagesFile(self):
        """Re-write all messages stored in memory onto file."""
        with open("Messages.txt", "w") as messageFile:
            for message in self.inboxAllAccounts:
                messageFile.write(message.PrintMessagesToTxt())


    def loadInbox(self):
        """Load all inbox messages on file into memory."""
        messagesFile = open('Messages.txt', 'r')
        messages = messagesFile.readlines()

        '''
        # UNUSED
        # Non-asterisk version of appending inbox messages
        for lineNum, lineText in enumerate(messages, 1):  # Number each message starting at 1
            if lineNum % 4 == 1:  # Username
                currentUser = lineText.strip()
            elif lineNum % 4 == 2:  # Recipient
                recipient = lineText.strip()
            elif lineNum % 4 == 3:  # Message text
                text = lineText.strip()
            elif lineNum % 4 == 0:  # New message boolean
                isNew = bool(lineText.strip())
                self.inboxAllAccounts.append(Message(currentUser, recipient, text, isNew))

                # debug print
                #print(currentUser, recipient, text, isNew)
        '''

        # Asterisk version of appending inbox messages
        astericksCount=0
        for line in messages:
        # count in text file seperate sections
            if(astericksCount ==1):
                currentUser = line.strip()
                astericksCount +=1
            if(astericksCount ==3):
                recipient = line.strip()
                astericksCount+=1
            if(astericksCount == 5):
                text = line.strip()
                astericksCount+=1
            if(astericksCount == 7):
                isNew = line.strip()
                if isNew == "False":
                    isNew = False
                else:
                    isNew = True
                astericksCount+=1
            if (line[0]=='*' and line[1]=='*'):
                astericksCount +=1
            if(astericksCount==8):
                self.inboxAllAccounts.append(Message(currentUser,recipient,text,isNew))
                astericksCount=0


    def ShowMessage(self,message):
        """Show an inbox message and present the user with a menu of message options."""
        print(message.Print())

        # Set a message's "new" status to false
        for msg in self.inboxAllAccounts:
            if msg == message:
                msg.isNew = False
                print(f"{msg.currentUsername} {msg.recipient} {msg.message} {msg.isNew}")
                self.UpdateMessagesFile()
                break

        global choice
        while True:
            choice = input(
                "\n" + "Enter [R] to reply" + '\n' \
                + "Enter [D] to delete message" + '\n' \
                + "Enter [Q] to return to the previous menu" + '\n')
            choice = choice.lower()

            if (choice == 'r'):  # Reply
                text = input('\nEnter the message you would like to send '+ message.currentUsername + ':\n' )
                self.SendMessage(globals.currentAccount.username,message.currentUsername,text)
                return

            elif (choice == 'd'):  # Delete
                for num, msg in enumerate(self.inboxAllAccounts):
                    if msg == message:
                        self.DeleteMessage(num)
                        self.UpdateMessagesFile()
                return

            elif (choice == 'q'):  # Quit
                return
        #quitLogic()


    def ShowPersonalInbox(self,currentUser):
        """Show all received messages and allow the user to view a message."""

        # Append each message addressed to the current user to a dictionary whose keys are numerically ordered
        while True:
            userMessages = dict()
            messageNum = 0
            for message in self.inboxAllAccounts:
                if message.recipient == currentUser:
                    messageNum += 1
                    userMessages[messageNum] = message

            # Message display
            print(f'\n{"#":<5}{"FROM":<20}{"FRIEND":<10}{"UNREAD":<6}')
            print('-' * 41)
            for num, message in userMessages.items():
                isFriend = None
                if globals.IsFriend(globals.currentAccount.username, message.currentUsername):
                    isFriend = "Y"
                else:
                    isFriend = "N"

                isNew = None
                if message.isNew:
                    isNew = "Y"
                else:
                    isNew = "N"

                print(f"{num:<5}" +
                    f"{message.currentUsername:<20}" +
                    f"{isFriend:<10}" +
                    f"{isNew:<6}")

            ans = input('\nEnter the number of the message you would like to view' +
                '\nEnter [Q] to return to the previous menu\n')
            if (ans.lower() == 'q'):
                return False
            try:
                ans = int(ans)
            except ValueError:  # Input is not an integer
                print('\nIncorrect input\n')
                continue
            try:
                self.ShowMessage(userMessages.get(ans))
            except AttributeError:   # Email number does not exist
                print('\nIncorrect input\n')
                continue

    '''
    def ShowPersonalInbox(self,currentUser):
        i=1
        j=0
        for message in range(len(self.inboxAllAccounts)):
            if str(self.inboxAllAccounts[message].recipient) == str(currentUser):
                print(i,'From: ',self.inboxAllAccounts[message].currentUsername,'\n')
                i+=1
        i=0
        j=0
        ans = input('\nEnter the number of the message you would like to view\nEnter [Q] to quit looking at the inbox')

        if (ans.lower == 'q'):
            return False
        else:
            try:
                ans = int(ans)
            except ValueError:
                ans = input('\nIncorrect input\nEnter the number of the message you would like to view\nEnter [Q] to quit looking at the inbox')
            if(type(ans)==int):
                for message in range(len(self.inboxAllAccounts)):
                    if str(self.inboxAllAccounts[message].recipient) == str(currentUser):
                        i+=1
                    if(i==ans):
                        self.ShowMessage(self.inboxAllAccounts[j])
                    j+=1
    '''

    #def DeleteMessage(self, messageToDelete,index):
    def DeleteMessage(self, index):
        """Delete a message stored in memory."""
        self.inboxAllAccounts.pop(index)
        print("\nMessage deleted!\n")
