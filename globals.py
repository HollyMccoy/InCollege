# Global variables and functions


def Initialize():
    """Initialize non-static global variables."""
    global currentAccount  # Current logged-in account
    global goBack  # The character used to go back to the previous menu
    global loggedIn  # Whether or not the current user is logged in
    global students  # List of all saved accounts
    global jobs      # List of jobs
    global myApplications  # List of applications submitted by current user
    global savedJobs #List of jobs that you have saved
    goBack = 'q'
    loggedIn = False
    students = []
    jobs = []
    myApplications = []
    savedJobs = []

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
            '\n' + f"[{goBack.upper()}] Return to the previous menu" + '\n\n').lower()
        if selection == goBack:
            break
