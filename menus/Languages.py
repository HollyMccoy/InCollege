# Menu commands for the "Languages" submenu
# Path: Main menu / important links / privacy policy / guest controls / languages

import globals
from InCollege import goBack

def ShowMenu():
    """Present the user with a menu of guest control settings."""
    while True:
        selection = input(
            "\n" + "-- Languages --: " + '\n\n' \
            + f"Current language: {globals.currentAccount.language}" + '\n\n' \
            + "[1] English" + '\n' \
            + "[2] Spanish" + '\n' \
            + f"[{goBack.upper()}] Quit" + '\n\n')
        selection = selection.lower()

        if (selection == "1"):
            globals.currentAccount.language = "English"
            '''
            with open("Logins.txt", "a+") as text_file:
                text_file.seek(0)
                while True:
                    #line = text_file.readline().rstrip().split()
                    account = text_file.readline().rstrip().split()
                    if account:
                        if globals.currentAccount.username == account[0]:
                            print(f"ACCOUNT FOUND: {account[0]}")
                            print(f"{globals.currentAccount.Print()}", file=text_file)
                            break
                    else:
                        break
            '''
        elif (selection == "2"):
            globals.currentAccount.language = "Spanish"
            '''
            with open("Logins.txt", "a+") as text_file:
                text_file.seek(0)
                while True:
                    #line = text_file.readline().rstrip().split()
                    account = text_file.readline().rstrip().split()
                    if account:
                        if globals.currentAccount.username == account[0]:
                            print(f"ACCOUNT FOUND: {account[0]}")
                            print(f"{globals.currentAccount.Print()}", file=text_file)
                            break
                    else:
                        break
            '''
        elif (selection == goBack):
            return
