# Global variables


def Initialize():
    """Initialize non-static global variables."""
    global currentAccount  # Current logged-in account
    global goBack  # The character used to go back to the previous menu
    global loggedIn  # Whether or not the current user is logged in
    global students  # List of all saved accounts

    goBack = 'q'
    loggedIn = False
    students = []


def updateAccounts():
    """Update the current account's information and then save all accounts to the login file."""
    for account in students:
        if account == currentAccount:  # Check if the current account matches one within the list of students
            account.copy(currentAccount)  # Copy the current account's information to the list account
            with open("logins.txt", "w") as text_file:
                [print(student.Print(), file=text_file) for student in students]  # Write all accounts to the login file
                break
