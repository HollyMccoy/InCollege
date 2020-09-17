#include User.py
from User import User
import sys




# for create account option
def CreateAccount():
    if (len(students) == 5):
        print('Current max of accounts reached, please delete an account to make a new one')
        return
    # must check if max account #'s is reached

    # bool for whether password is valid
    validPass = False
    # take in username
    inputUser = input("Please enter a username:")
    # ** this is where we should validate username  (not the same as another username)

    #take in password
    inputPass = input("Please enter a password (must conatin 8 to 12 characters, one capital letter, one digit, and one symbol) :")
    # below should also confirm password is valid ( minimum of 8 characters), (maximum of 12 characters), (at least one capital letter), (one digit), (one non-alpha character)


    #once username and password are deemed valid, place new user in .txt file and array
    students.append(User(inputUser, inputPass))
    for i in students:
        print(i.Print())
        logins.write(i.Print())
    ## logins.truncate(0)   this is the erase file function in case accounts must be rewritten


def LoginToAccount():
    # take in username
    inputUser = input("Please enter a username: ")
    # take in password
    inputPass = input("Please enter a password: ")
    # looks through each account, sends it straight to ChackLogin() and when one returns true it will set as current Account and inform user login was a success
    for account in students:
        if(account.CheckLogin(inputUser,inputPass)):
            currentAccount = account
            print('Login successful welcome to InCollege')
            return
    return False





# include function to call from CreateAccount()  that would create account (change user and pass from "NULL") then add info to some .txt file for permanent storage

# include function that upon starting InCollege app would open .txt file and create already existing accounts / add them to array


# need function to check if any account spots are left


#def FreeSpace ():




def mainMenu():
    # create array of size max # of students
    global students
    global logins
    global currentAccount

    logins = open('Logins.txt', 'r+')
    students = []

    # this is where we at first should intercept and load text file accounts
    print("Would you like to sign in or create an account?" + '\n' + "Press [L] to Login" + '\n' + "Press [C] to create an account")
    choice = input()
    choice = choice.lower()
    while choice != 'q':
    #present menu options (still missing a few options

    #this could probs be a switch so I will SWITCH it to that haha fml

        if (choice == 'c'):
            CreateAccount()
        elif (choice == 'l'):
             LoginToAccount()

        print("Would you like to sign in or create an account?" + '\n' + "Press [L] to Login" + '\n' + "Press [C] to create an account")
        choice = input()
        choice = choice.lower()

if __name__ == "__main__":
        mainMenu()
