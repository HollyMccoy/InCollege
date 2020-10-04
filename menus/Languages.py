# Menu commands for the "Languages" submenu
# Path: Main menu / important links / privacy policy / guest controls / languages

import globals


def ShowMenu():
    """Present the user with a menu of guest control settings."""
    while True:
        selection = input(
            "\n" + "-- Languages --: " + '\n\n' \
            + f"Current language: {globals.currentAccount.language}" + '\n\n' \
            + "[1] English" + '\n' \
            + "[2] Spanish" + '\n' \
            + f"[{globals.goBack.upper()}] Return to the previous menu" + '\n\n')
        selection = selection.lower()

        if (selection == "1"):
            globals.currentAccount.language = "English"
            globals.updateAccounts()
        elif (selection == "2"):
            globals.currentAccount.language = "Spanish"
            globals.updateAccounts()
        elif (selection == globals.goBack):
            return
