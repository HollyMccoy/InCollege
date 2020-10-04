# Menu commands for the "Important Links" submenu
# Path: Main menu / important links

import globals
from menus import GuestControls


def ShowMenu():
    """Present the user with a menu of important InCollege links."""
    filePath = "docs\\ImportantLinks\\"
    while True:
        selection = input(
            "\n" + "-- Important links --" + '\n\n' \
            + "[1] About" + '\n' \
            + "[2] Accessibility" + '\n' \
            + "[3] Brand Policy" + '\n' \
            + "[4] Cookie Policy" + '\n' \
            + "[5] Copyright Notice" + '\n' \
            + "[6] Copyright Policy" + '\n' \
            + "[7] Privacy Policy" + '\n' \
            + "[8] User Agreement" + '\n' \
            + f"[{globals.goBack.upper()}] Return to the previous menu" + '\n\n')
        selection = selection.lower()

        if (selection == '1'):
            ShowAbout(filePath, "About.txt")
        elif (selection == '2'):
            ShowAccessibility(filePath, "Accessibility.txt")
        elif (selection == '3'):
            ShowBrandPolicy(filePath, "BrandPolicy.txt")
        elif (selection == '4'):
            ShowCookiePolicy(filePath, "CookiePolicy.txt")
        elif (selection == '5'):
            ShowCopyrightNotice(filePath, "CopyrightNotice.txt")
        elif (selection == '6'):
            ShowCopyrightPolicy(filePath, "CopyrightPolicy.txt")
        elif (selection == '7'):
            ShowPrivacyPolicy(filePath, "PrivacyPolicy.txt")
        elif (selection == '8'):
            ShowUserAgreement(filePath, "UserAgreement.txt")
        elif (selection == globals.goBack):
            return


def PrintFile(filePath, fileName):
    """Read and print the contents of a specified text file."""
    with open(filePath + fileName) as file:
        lines = file.readlines()
        [print(line, end='') for line in lines]


def ShowAbout(filePath, fileName):
    """Print out the About document."""
    print("-- About -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowAccessibility(filePath, fileName):
    """Print out the accessibility document."""
    print("-- Accessibility -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowBrandPolicy(filePath, fileName):
    """Print out the brand policy."""
    print("-- Brand Policy -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowCookiePolicy(filePath, fileName):
    """Print out the cookie policy."""
    print("-- Cookie Policy -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowCopyrightNotice(filePath, fileName):
    """Print out the copyright notice."""
    print("-- Copyright Notice -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowCopyrightPolicy(filePath, fileName):
    """Print out the copyright policy."""
    print("-- Copyright Policy -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()


def ShowPrivacyPolicy(filePath, fileName):
    """Print out the privacy policy AND~~~~~~~~~~."""
    print("-- Privacy Policy -- " + "\n")
    PrintFile(filePath, fileName)
    while globals.loggedIn:
        selection = GuestControls.ShowMenu()
        if (selection == globals.goBack):
            break
    if not globals.loggedIn:
        globals.ReturnPrompt()

def ShowUserAgreement(filePath, fileName):
    """Print out the user agreement."""
    print("-- User Agreement -- " + "\n")
    PrintFile(filePath, fileName)
    globals.ReturnPrompt()
