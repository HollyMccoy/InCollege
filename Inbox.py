from Message import Message
class Inbox:
    

    def __init__(self):
        self.inboxAllAccounts=[]

    def SendMessage(self,currentUser,recipient,text):
        self.inboxAllAccounts.append(Message(str(currentUser),recipient,text,True))
        with open("Messages.txt", "a+") as file1:
                file1.write(self.inboxAllAccounts[len(self.inboxAllAccounts)-1].PrintMessagesToTxt()) 
        return


    def loadInbox(self):
        messagesFile = open('Messages.txt', 'r')
        messages = messagesFile.readlines()
        
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
                isNew = bool(line.strip())
                astericksCount+=1
            if (line[0]=='*' and line[1]=='*'):
                astericksCount +=1
            if(astericksCount==8):
                self.inboxAllAccounts.append(Message(currentUser,recipient,text,isNew))
                astericksCount=0

    def ShowMessage(self,message):
        print(message.Print())
        
        global choice
        while True:
            choice = input(
                "\n" + "Enter [R] to reply" + '\n' \
                + "Enter [D] to delete message" + '\n' \
                + "Enter [Q] to return to the previous menu" + '\n')
            choice = choice.lower()

            if (choice == 'r'): 
                #
                #
                # Reply function here
                #
                #
                print("under construction")
            elif (choice == 'd'): 
                #
                #
                # Delete function here
                #
                #
                print("under construction")
            elif (choice == 'q'):  
                return False

        quitLogic()


    def ShowPersonalInbox(self,currentUser):
        i=1
        j=0
        for message in range(len(self.inboxAllAccounts)):
            if str(self.inboxAllAccounts[message].recipient) == str(currentUser):
                print(i,'From: ',self.inboxAllAccounts[message].currentUsername,'\n')
                i+=1
        i=0
        j=0
        ans = input('\nEnter the number of the message you would like to view\nEnter [Q] to quit lookinf at the inbox')
        
        if (ans.lower == 'q'):
            return False
        else: 
            try:
                ans = int(ans)
            except ValueError:
                ans = input('\nIncorrect input\nEnter the number of the message you would like to view\nEnter [Q] to quit lookinf at the inbox')
            if(type(ans)==int):
                 
                for message in range(len(self.inboxAllAccounts)):
                     
                    if str(self.inboxAllAccounts[message].recipient) == str(currentUser):
                        i+=1
                        

                    if(i==ans):   
                        self.ShowMessage(self.inboxAllAccounts[j])


                j+=1
                        



   

                
    def DeleteMessage(self, messageToDelete,index):
        self.inboxAllAccounts.pop(index)
