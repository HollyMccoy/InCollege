#include User.py
from User import User




# for create account option
def CreateAccount():
    # must check if max account #'s is reached

    # bool for whether password is valid
    validPass = false
    # take in username
    inputUser = input("Please enter a username:")
    # ** this is where we should validate username  (not the same as another username)

    #take in password
    inputPass = input("Please enter a password (must conatin 8 to 12 characters, one capital letter, one digit, and one symbol) :")
    # below should also confirm password is valid ( minimum of 8 characters), (maximum of 12 characters), (at least one capital letter), (one digit), (one non-alpha character)


    #once username and password are deemed valid, place new user in .txt file and array




def LoginToAccount():
    input("Please enter a username:")





# include function to call from CreateAccount()  that would create account (change user and pass from "NULL") then add info to some .txt file for permanent storage

#include function that upon starting InCollege app would open .txt file and create already existing accounts / add them to array





def main():
    # create array of size max # of students
    students = []
    # this is where we at first should intercept and load text file accounts
    for i in range(5) :
        students.append(User())
    #present menu options (still missing a few options
    print("Would you like to sign in or create an account?" + '\n' + "Press [L] to Login"+ '\n' + "Press [C] to create an account")
    choice = input()
    choice = choice.lower()
    #this could probs be a switch so I will SWITCH it to that haha fml
    if (choice == 'c'):
        CreateAccount()
    elif (choice == 'l'):
        LoginToAccount()



if __name__ == "__main__":
        main()