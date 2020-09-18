#include User.py
from User import User
import sys

def ValidatePassword(input):
    num = False
    nonalpha = False
    capital = False
    length = False
    if (len(input) >= 8):
            if (len(input) <= 12):
                length =True
    for symbol in input:
        if symbol.isnumeric():
            num = True
            print(symbol)
        elif (symbol.isalnum() == False):
            nonalpha = True
            print(symbol)
        elif symbol.isupper():
            capital = True
            print(symbol)
    if length:
        if num:
            if nonalpha:
                if capital:
                    print('returning true')
                    return True
    return False
def ValidateUser(input):
    for account in students:
        if (account.username == input):
            return False
    if (input.isalnum() ==False):
        return False
    return True
def LoadAccounts():
    logins = open('Logins.txt', 'r')
    userPass = logins.readlines()
    
    for account in userPass:
        credentials = account.split()
        students.append(User(credentials[0], credentials[1]))
    #userPass = userPass.split()
    #print(userPass)
#students.append(User(userPass[0],userPass[1]))
# for create account option
def CreateAccount():
    validUser = False
    validPass = False
    global choice
    if (len(students) >= 5):
        print('All permitted accounts have been created, please come back later')
        return
    # must check if max account #'s is reached

    # bool for whether password is valid
    
    # take in username
    while (validUser == False):
        inputUser = input("Please enter a UNIQUE username without spaces:")
        validUser = ValidateUser(inputUser)

    # ** this is where we should validate username  (not the same as another username)

    #take in password
    while (validPass == False): 
        inputPass = input("Please enter a password (must conatin 8 to 12 characters, one capital letter, one digit, and one symbol) :")
        validPass = ValidatePassword(inputPass)
        # below should also confirm password is valid ( minimum of 8 characters), (maximum of 12 characters), (at least one capital letter), (one digit), (one non-alpha character)


    #once username and password are deemed valid, place new user in .txt file and array
    students.append(User(inputUser, inputPass))
    with open("Logins.txt", "a+") as text_file:
           print("{}".format(students[len(students)-1].Print()), file=text_file)

    print('Account successfully created!')
    
    ## logins.truncate(0)   this is the erase file function in case accounts must be rewritten
def LoginToAccount():
    global choice
    # take in username
    inputUser = input("Please enter a username: ")
    # take in password
    inputPass = input("Please enter a password: ")
    # looks through each account, sends it straight to ChackLogin() and when one returns true it will set as current Account and inform user login was a success
    for account in students:
        if(account.CheckLogin(inputUser,inputPass)):
            currentAccount = account
            print('You have successfully logged in')
            choice = 'q'
            return
    print('Incorrect username / password, please try again')
    LoginToAccount()

    return 
# include function to call from CreateAccount()  that would create account (change user and pass from "NULL") then add info to some .txt file for permanent storage
# include function that upon starting InCollege app would open .txt file and create already existing accounts / add them to array
# need function to check if any account spots are left
#def FreeSpace ():
def mainMenu():
    # create array of size max # of students
    
    global students
    global logins
    global currentAccount
    global choice
    
    logins = open('Logins.txt', 'a+')
    choice = 'd'
    students = []
    LoadAccounts()
    # this is where we at first should intercept and load text file accounts
   
    while choice != 'q':
    #present menu options (still missing a few options
      choice = input("Would you like to sign in or create an account?" + '\n' + "Press [L] to Login" + '\n' + "Press [C] to create an account"+'\n' + "Press [Q] to quit" + '\n')
      choice = choice.lower()
    #this could probs be a switch so I will SWITCH it to that haha fml

      if (choice == 'c'):
           CreateAccount()
      elif (choice == 'l'):
           LoginToAccount()

    choice = 'ah'
    while choice != 'q':
      choice = input("press [F] to find someone" + '\n' + "Press [J] to look for a job" + '\n' + "Press [L] to learn a new skill"+'\n' + "Press [Q] to quit" + '\n')
      choice = choice.lower()

      if (choice == 'f'):
           print("under construction")
      elif (choice == 'j'):
           print("under construction")
      elif (choice == 'l'):
           print("under construction")
      
      
        

if __name__ == "__main__":
        mainMenu()
