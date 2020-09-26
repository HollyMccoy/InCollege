# include User.py
from User import User
from Job import Job
import sys, time


def ShowLoggedOutMenu():
    """Present menu options for when the user is logged out."""
    global choice
    choice = input(
        "\n" + "Would you like to sign in or create an account?" + '\n' \
        + "Press [L] to login" + '\n' \
        + "Press [C] to create an account" + '\n' \
        + "Press [F] to find someone" + '\n' \
        + "Press [W] to watch a video" + '\n' \
        + f"Press [{goBack.upper()}] to quit" + '\n')
    choice = choice.lower()


def ShowLoggedInMenu():
    """Present menu options for when the user is logged in."""
    global choice
    choice = input(
        "\n" + "Press [F] to find someone" + '\n' \
        + "Press [J] to look for a job" + '\n' \
        + "Press [P] to post a job" + '\n' \
        + "Press [L] to learn a new skill" + '\n' \
        + f"Press [{goBack.upper()}] to log out" + '\n')
    choice = choice.lower()


# Redundant; saved for future reference
"""
def ShowInviteMenu():
    # Invite the user to login or create an account if they find a contact while logged out.
    global choice
    choice = input(
        "\n" + "Join your friends today by logging in or creating an account" + "\n" \
        + "Press [L] to login" + "\n" \
        + "Press [C] to create an account" + "\n" \
        + f"Press [{goBack}] to return to the previous menu")
    choice = choice.lower()
"""


def SuccessStory():
    """Print out a student success story."""
    print()
    Story = open('SuccessStory.txt', 'r')
    line = Story.readline()
    while line:
        print(line)
        line = Story.readline()
    print()


def ValidatePassword(input):
    """Check if a password meets security criteria."""
    num = False
    nonalpha = False
    capital = False
    length = False
    if (len(input) >= 8):
        if (len(input) <= 12):
            length = True
    for symbol in input:
        if symbol.isnumeric():
            num = True

        elif (symbol.isalnum() == False):
            nonalpha = True

        elif symbol.isupper():
            capital = True

    if length:
        if num:
            if nonalpha:
                if capital:
                    return True
    return False


def ValidateUser(input):
    """Check whether the username is unique and contains only alpha-numeric characters."""
    for account in students:
        if (account.username == input):
            return False
    if (input.isalnum() == False):
        return False
    return True


def LoadJobs():
    """Read in all jobs that are stored within file."""
    listings = open('Jobs.txt', 'r')
    # each line in job.txt is a listing for a job opening.
    # openings = all the lines in job.txt which is stored in listings
    Openings = listings.readlines()

    for job in Openings:
        details = job.split()
        jobs.append(Job(details[0], details[1], details[2], details[3], details[4]))


def LoadAccounts():
    """Read in all accounts that are stored within file."""
    logins = open('Logins.txt', 'r')
    userPass = logins.readlines()

    for account in userPass:
        if account:
            credentials = account.split()
            students.append(User(credentials[0], credentials[1], credentials[2], credentials[3]))
    # userPass = userPass.split()
    # print(userPass)


def CreateJob():
    """Create a new job posting."""
    if (len(jobs) >= 5):
      print('\n' + 'All permitted job postings have been created, please come back later')
      return
    title = input("Enter the job title: ")
    description = input("Enter a job description: ")
    employer = input("Enter the employer: ")
    location = input("Enter the job location: ")
    salary = int(input("Enter salary (do not include and non-numerical characters): "))
    jobs.append(Job(title, description, employer, location, salary))
    with open("Jobs.txt", "a+") as file1:
        print("{}".format(jobs[len(jobs) - 1].Print()), file=file1)


# for create account option
def CreateAccount():
    """Create a new user account."""
    validUser = False
    validPass = False
    global choice
    if (len(students) >= 5):
        print('\n' + 'All permitted accounts have been created, please come back later')
        return

    # must check if max account #'s is reached
    # bool for whether password is valid

    # take in username
    while (validUser == False):
        inputUser = input("\n" + "Please enter a UNIQUE username without spaces:")
        validUser = ValidateUser(inputUser)

    # ** this is where we should validate username  (not the same as another username)

    # take in password
    while (validPass == False):
        inputPass = input(
            "Please enter a password (must conatin 8 to 12 characters, one capital letter, one digit, and one symbol) :")
        validPass = ValidatePassword(inputPass)
        # below should also confirm password is valid ( minimum of 8 characters), (maximum of 12 characters), (at least one capital letter), (one digit), (one non-alpha character)

    # take in first name
    inputFirstName = input("Please enter your first name: ")

    # take in last name
    inputLastName = input("Please enter your last name: ")

    # once username and password are deemed valid, place new user in .txt file and array
    students.append(User(inputUser, inputPass, inputFirstName, inputLastName))
    with open("Logins.txt", "a+") as text_file:
        print("{}".format(students[len(students) - 1].Print()), file=text_file)

    print('Account successfully created!')

    ## logins.truncate(0)   this is the erase file function in case accounts must be rewritten


def LoginToAccount():
    """Attempt to log the user into an account."""
    global choice
    global loggedIn

    while True:
        # take in username
        inputUser = input("\n" + "Please enter a username: ")

        # take in password
        inputPass = input("Please enter a password: ")

        # looks through each account, sends it straight to CheckLogin() and when one returns true it will set as current Account and inform user login was a success
        for account in students:
            if (account.CheckLogin(inputUser, inputPass)):
                currentAccount = account
                print('You have successfully logged in')
                choice = 'ah'
                loggedIn = True
                return

        # Display an error message if the login fails
        # Allow the user to try again or go back
        while True:
            choice = input(
                '\n' + 'Incorrect username / password.' + '\n\n' \
                'Press [L] to try again.' + '\n' \
                f'Press [{goBack.upper()}] to return to the previous menu.' + '\n')
            choice = choice.lower()
            if choice == goBack:
                return
            elif choice == 'l':
                break
            else:
                continue


def FindContact():
    """Allow the user to search for someone by specifying a first and last name."""
    names = list()
    found = False

    # Append all first and last names of users to a list
    with open("Logins.txt", "r") as userFile:
        while True:
            userInfo = userFile.readline()
            if userInfo:
                userInfo = userInfo.split()
                names.append({"firstName": userInfo[2], "lastName": userInfo[3]})
            else:
                break

    firstName = input("\n" + "Enter first name: ")
    lastName = input("Enter last name: ")

    # Search the list of names for a matching first and last name
    for name in names:
        print(name.get('firstName'), name.get('lastName'))
        if firstName == name.get('firstName') and lastName == name.get('lastName'):
            found = True
            print("\n" + "They are a part of the InCollege system.")
            break
    if not found:
        print("\n" + "They are not yet a part of the InCollege system.")

    if found and not loggedIn:
        #ShowInviteMenu()
        print("Join your friends today by signing in or creating an account.")

def JobSearch():
    """NOT YET IMPLEMENTED: Allow the user to search for a job."""
    print("\n" + "Under construction")


def LearnSkill():
    """Present the user with a numbered list of skills to learn."""
    # Number each skill within the file and add it to a dictionary
    skills = dict()
    with open("Skills.txt", "r") as skillFile:
        [skills.update({str(skillNum): skill.rstrip()}) for skillNum, skill in enumerate(skillFile.readlines(), 1)]
    print()

    # Prompt the user to select a skill
    while True:
        [print(f'Press [{skillNum}] to learn about {skill.lower()}') for skillNum, skill in skills.items()]
        print(f"Press [{goBack.upper()}] to return to the previous menu")

        selection = input("")
        selection = selection.lower()
        if selection in skills.keys():
            print("Under construction" + "\n")
        elif selection == goBack:
            break
        elif selection not in skills.keys():
            continue


# include function to call from CreateAccount()  that would create account (change user and pass from "NULL") then add info to some .txt file for permanent storage
# include function that upon starting InCollege app would open .txt file and create already existing accounts / add them to array
# need function to check if any account spots are left
# def FreeSpace ():
def mainMenu():
    """Show the main menus to the user."""
    # create array of size max # of students

    global students
    global logins
    global loggedIn
    global currentAccount
    global choice
    global goBack
    global jobs
    logins = open('Logins.txt', 'a+')
    loggedIn = False
    choice = 'd'
    goBack = 'q'
    students = []
    jobs = []

    LoadAccounts()
    # this is where we at first should intercept and load text file accounts
    SuccessStory()

    while True:  # Logged in and logged out menu loop

        #while choice != 'q' and choice != 'ah':
        while not loggedIn:
            ShowLoggedOutMenu()

            # this could probs be a switch so I will SWITCH it to that haha fml
            if (choice == 'c'):
                CreateAccount()
            elif (choice == 'l'):
                LoginToAccount()
                #if (LoginToAccount()):
                #    continue
            elif (choice == 'f'):
                FindContact()
            elif (choice == 'w'):
                print("\n" + "Video is now playing")
                time.sleep(20)
                print("Video ending...")
                time.sleep(3)
            elif (choice == goBack): # Break out of the inner loop
                break

        if (choice == goBack): # Break out of the outer loop to exit the program
            break

        #choice = 'ah'
        #while choice != 'q':
        while loggedIn:
            ShowLoggedInMenu()

            if (choice == 'f'):
                FindContact()
            elif (choice == 'j'):
                JobSearch()
            elif (choice == 'l'):
                LearnSkill()
            elif (choice == 'p'):
                CreateJob()
            elif (choice == goBack):  # Break out of the inner loop and show the logged out menu
                loggedIn = False
                break


if __name__ == "__main__":
    mainMenu()
