# Global variables

def Initialize():
    """Initialize non-static global variables."""
    global currentAccount  # Current logged-in account
    global loggedIn  # Whether or not the current user is logged in
    global students  # List of all saved accounts

    loggedIn = False
    students = []
