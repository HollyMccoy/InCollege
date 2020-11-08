# Global variables and functions


def Initialize():
    """Initialize non-static global variables."""
    global currentAccount  # Current logged-in account
    global goBack  # The character used to go back to the previous menu
    global loggedIn  # Whether or not the current user is logged in
    global students  # List of all saved accounts
    global jobs      # List of jobs
    global myApplications  # List of applications submitted by current user
    global savedJobs  # List of jobs that you have saved
    global deletedJobs  # List of jobs that have been deleted

    goBack = 'q'
    loggedIn = False
    students = []
    jobs = []
    myApplications = []
    savedJobs = []
    deletedJobs = []


def updateAccounts():
    """Update the current account's information and then save all accounts to the login file."""
    for account in students:
        if account == currentAccount:  # Check if the current account matches one within the list of students
            account.copy(currentAccount)  # Copy the current account's information to the list account
            with open("logins.txt", "w") as text_file:
                [print(student.Print(), file=text_file) for student in students]  # Write all accounts to the login file
                break


def ReturnPrompt():
    """Prompt the user to return to the previous menu after reaching a terminal menu option."""
    while True:
        selection = input(
            '\n' + f"Press [{goBack.upper()}] to return to the previous menu" + '\n').lower()
        if selection == goBack:
            print()
            break


def AccountExists(username):
    """Determine whether the specified account exists."""
    accountExists = False
    with open("Logins.txt", "r") as loginFile:
        logins = loginFile.read().splitlines()
        for line in logins:
            if line.split()[0] == username:
                accountExists = True
                break
    return accountExists


def IsFriend(user, other):
    """Returns whether two users are friends."""
    friendship = False
    with open("Friends.txt", "r") as friendsListFile:
        friendsList = friendsListFile.read().splitlines()
        for line in friendsList:
            if (user in line) and (other in line):
                friendship = True
                break
    return friendship


def CanSendMessage(user, other):
    """Returns whether a user is eligible to send a message to another user."""
    canSend = False
    if IsFriend(user, other):
        canSend = True
    if currentAccount.accountPlus == True:
        canSend = True
    return canSend

def strToBool(str):
        if str == "True":
            return True
        elif str == "False":
            return False
        else:
            raise Exception("Error converting string to boolean")

'''
def IsPlusAccount(user):
    """Returns whether a user has a "Plus" account."""
    plusAccount = False
    with open("Logins.txt", "r") as loginFile:
        logins = loginFile.read().splitlines()
        for login in friendsList:
            if (user in line) and (other in line):
                friendship = True
                break
    return plusAccount

def IsPlusAccount2(user):
    """Returns whether a user has a "Plus" account."""
    plusAccount = False
    with open("Logins.txt", "r") as loginFile:
        logins = loginFile.read().splitlines()
        for login in friendsList:
            if (user in line) and (other in line):
                friendship = True
                break
    return plusAccount
'''
