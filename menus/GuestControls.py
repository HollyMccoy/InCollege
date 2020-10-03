# Menu commands for the "Guest Controls" submenu
# Path: Main menu / important links / privacy policy / guest controls

import globals
from menus import Languages


def ShowMenu():
    """Present the user with a menu of guest control settings."""
    while True:
        selection = input(
            "\n" #+ "Choose an option: " + '\n\n' \
            + "[1] Guest Controls" + '\n' \
            + f"[{globals.goBack.upper()}] Quit" + '\n\n')
        selection = selection.lower()

        if (selection == "1"):
            ShowGuestControls()
        elif (selection == globals.goBack):
            return selection


def ShowGuestControls():
    """Show guest control settings that are saved to the user's profile."""
    while True:
        selection = input(
            "\n" + "-- Guest Controls --" + '\n\n' \
            + f"[1] InCollege email alerts: {globals.currentAccount.emailAlerts}" + '\n' \
            + f"[2] SMS alerts: {globals.currentAccount.textAlerts}" + '\n' \
            + f"[3] Targeted advertising: {globals.currentAccount.targetedAdvertising}" + '\n' \
            + f"[4] Languages: {globals.currentAccount.language}" + '\n' \
            + f"[{globals.goBack.upper()}] Quit" + '\n\n')
        selection = selection.lower()

        if (selection == "1"):
            globals.currentAccount.emailAlerts = not globals.currentAccount.emailAlerts
            globals.updateAccounts()
        elif (selection == "2"):
            globals.currentAccount.textAlerts = not globals.currentAccount.textAlerts
            globals.updateAccounts()
        elif (selection == "3"):
            globals.currentAccount.targetedAdvertising = not globals.currentAccount.targetedAdvertising
            globals.updateAccounts()
        elif (selection == "4"):
            Languages.ShowMenu()
        elif (selection == globals.goBack):
            break
