# include User.py
from Job import Job, Experience
from User import User
from Profile import Profile
from School import School
from menus import ImportantLinks
from Application import Application
import globals
import sys, time
from datetime import date
from Inbox import Inbox

inbox = Inbox()

def ToPascal(s):
    return (''.join(x for x in s.title() if not x.isspace()))


def SuccessStory():
    """Print out a student success story."""
    print()
    Story = open('SuccessStory.txt', 'r')
    line = Story.readline().rstrip()
    while line:
        print(line)
        line = Story.readline().rstrip()
    print()
    # Validation methods


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
    for account in globals.students:
        if (account.username == input):
            return False
    if (input.isalnum() == False):
        return False
    return True


def ValidateDate(input):
    """Check whether the date entered is in iso format"""
    try:
        date.fromisoformat(input)
        return True
    except:
        return False


def ValidateDegree(input):
    """Check whether the user entered a valid degree"""
    if (input == "Associate" or input == "Bachelor" or input == "Master" or input == "Doctorate"):
        return True
    else:
        return False
    # start/loading methods


def LoadAccounts():
    """Read in all accounts that are stored within file."""
    logins = open('Logins.txt', 'r')
    userPass = logins.readlines()

    for account in userPass:
        if len(account.split()) == 8:  # Determine if an account has the correct number of parameters
            credentials = account.split()
            globals.students.append(User(credentials[0],
                                         credentials[1],
                                         credentials[2],
                                         credentials[3],
                                         credentials[4],
                                         credentials[5],
                                         credentials[6],
                                         credentials[7]))
        else:
            print("Warning: invalid data in logins.txt")
            break
    # userPass = userPass.split()
    # print(userPass)


def LoadRequests():
    """Read in all accounts that are stored within file."""
    requestFile = open('Requests.txt', 'r')
    requestList = requestFile.readlines()

    for r in requestList:
        if len(r.split()) == 2:
            users = r.split()
            requests.append(users)


def LoadJobs():
    """Read in all jobs that are stored within file."""
    listings = open('Jobs.txt', 'r')
    # each line in job.txt is a listing for a job opening.
    # openings = all the lines in job.txt which is stored in listings
    Openings = listings.readlines()
    for job in Openings:
        details = job.split()
        if len(details) == 6:
            globals.jobs.append(Job(details[0], details[1], details[2], details[3], details[4], details[5]))


def LoadFriendsList():
    # friendsList = []
    with open("Friends.txt", "r") as friendsListFile:
        while True:
            friendsList = friendsListFile.readline()
            if friendsList:
                friendsList = friendsList.split()
                friendsLists.append(friendsList)
            else:
                break


def LoadMyApplications():
    applicationsFile = open('Applications.txt', 'r')
    applicationsList = applicationsFile.readlines()

    # check every 9 lines (9 lines are takenup by each application)
    # if username matches and the full description matches then add to currently logged in list
    if (len(applicationsList) < 8):
        return
    for a in range(len(applicationsList) % 9 + 1):
        i = 0
        if (applicationsList[a * 9].strip() != globals.currentAccount.username):
            continue
        while (i < len(globals.jobs)):
            if (globals.jobs[i].description.strip() == applicationsList[a * 9 + 2].strip()):
                globals.myApplications.append(
                    Application(applicationsList[a * 9 + 6].strip(), applicationsList[a * 9 + 7].strip(),
                                applicationsList[a * 9 + 8].strip(), globals.jobs[i], globals.currentAccount.username))

            i += 1

def LoadMessages():
    inbox.loadInbox()


# Friend list features
def ViewRequests():
    user = str(globals.currentAccount.username)
    print("You have sent a request to these users: ")
    for r in requests:
        if r[0] == user:
            print(r[1])


def FindNotification():
    """Informs the user of their most recent friend request, if any"""
    user = globals.currentAccount.username
    numMessages=0
    for i in range(len(inbox.inboxAllAccounts)):
        if (str(inbox.inboxAllAccounts[i].recipient.strip()) == str(globals.currentAccount.username) and inbox.inboxAllAccounts[i].isNew):
            numMessages+=1
    if(numMessages>0):
        print('\nYou have recieved '+str(numMessages)+' message(s), check your inbox!\n')


    for r in requests:
        if r[0] == user:
            selection = input("You have a friend request from " + r[1] + ". Do you accept? (y/n) \n")
            if selection.lower() == 'y':
                AddFriends(r[1])
        else:
            print(r[0] + " does not equal " + user + '\n')


def SendRequest(secondUser):
    """Sends a request from the current user to secondUser"""
    firstUser = str(globals.currentAccount.username)
    for r in requests:
        if (r[0] == firstUser and r[1] == secondUser):
            print("Error: You have made this request already")
            return False
    requests.remove(r)
    r[0].append(firstUser)
    r[1].append(secondUser)
    requests.append(r)
    UpdateRequests()
    print('Sent friend request to ' + secondUser + " (under construction)")
    return True


def DeleteRequest(secondUser):
    """Removes a friend request"""
    firstUser = str(globals.currentAccount.username)
    for r in requests:
        if (r[0] == firstUser and r[1] == secondUser):
            break
    if not (r[0] == firstUser and r[1] == secondUser):
        print("Error: Request not found")
        return False  # for testing
    requests.remove(r)
    UpdateRequests()
    return True  # for testing


def UpdateRequests():
    """Overwrites Requests.txt to the most current state"""
    newList = ""
    with open("Requests.txt", "w") as requestFile:
        for r in requests:
            newList = newList + r[0] + ' ' + r[1] + '\n'
        print("{}".format(newList), file=requestFile)


def CreateFriendsList(newUser):
    newList = [newUser]
    friendsLists.append(newList)
    UpdateFriendsList()


def ViewFriendsList():
    firstIteration = True
    friendInput = ""
    num = 1
    user = str(globals.currentAccount.username)
    for friendsList in friendsLists:
        if (friendsList[0] == str(user)):
            for friend in friendsList:
                if (firstIteration):
                    firstIteration = False
                    print(f'{friend}s Friends: ')

                else:
                    print(f"Press [{num}] to view {friend}s menu")
                    num += 1

            friendInput = input("Make a selection: ")

            if friendInput.isnumeric():
                FriendMenu(friendsList[int(friendInput)])
            break


def AddFriends(secondUser):
    """Creates a connection between two friends"""
    firstUser = str(globals.currentAccount.username)
    for friendList1 in friendsLists:
        if (friendList1[0] == firstUser):
            break

    for friendList2 in friendsLists:
        if (friendList2[0] == secondUser):
            break
    if secondUser not in friendList2:
        print("Error: second person not found")
        return False  # for testing
    elif secondUser in friendList1:
        print("Error: already friends")
        return False  # for testing
    friendsLists.remove(friendList1)
    friendsLists.remove(friendList2)
    friendList1.append(secondUser)
    friendList2.append(firstUser)
    friendsLists.append(friendList1)
    friendsLists.append(friendList2)
    UpdateFriendsList()
    DeleteRequest(secondUser)
    return True  # for testing


def DeleteFriends(secondUser):
    """Removes a connection between two friends"""
    firstUser = str(globals.currentAccount.username)
    for friendList1 in friendsLists:
        if (friendList1[0] == firstUser):
            break

    for friendList2 in friendsLists:
        if (friendList2[0] == secondUser):
            break

    if secondUser not in friendList2:
        print("Error: second person not found")
        return False  # for testing
    elif secondUser not in friendList1:
        print("Error: already not friends")
        return False  # for testing
    friendsLists.remove(friendList1)
    friendsLists.remove(friendList2)
    friendList1.remove(secondUser)
    friendList2.remove(firstUser)
    friendsLists.append(friendList1)
    friendsLists.append(friendList2)
    UpdateFriendsList()
    return True  # for testing


def UpdateFriendsList():
    """Overwrites Friends.txt to the most current state"""
    newList = ""
    with open("Friends.txt", "w") as friendsListFile:
        for friendsList in friendsLists:
            for f in friendsList:
                newList = newList + f + ' '
            newList += '\n'
        print("{}".format(newList), file=friendsListFile)
        # Profiles methods


def ViewUserProfile(name):
    for profile in globals.profiles:
        if profile.username == name:
            print(f"{name}s Profile: \n")
            print(profile.Print())
            break


def LoadProfiles():
    """Read in all profiles that are stored within file,
    as well as the associated employment and education information
    from their respective files."""

    globals.profiles = []
    experience = []
    education = None

    profiles = open('Profiles.txt', 'r')
    profileList = profiles.readlines()

    expFile = open('Experiences.txt', 'r')
    expList = expFile.readlines()

    schoolFile = open('Education.txt', 'r')
    schoolList = schoolFile.readlines()

    for p in profileList:
        if len(p.split()) == 7:  # Determine if a profile has the correct number of parameters
            pInfo = p.split()

            for e in expList:
                if len(e.split()) == 7:
                    eInfo = e.split()
                    if eInfo[0] == pInfo[0]:  # Check if the profile username matches the experience username
                        experience.append(Experience(eInfo[1].replace("_", " "),
                                                     eInfo[2].replace("_", " "),
                                                     date.fromisoformat(eInfo[3]),
                                                     date.fromisoformat(eInfo[4]),
                                                     eInfo[5].replace("_", " "),
                                                     eInfo[6].replace("_", " "), ))

                    if len(experience) >= 3:
                        break

            for s in schoolList:
                if len(s.split()) == 4:
                    sInfo = s.split()
                    if sInfo[0] == pInfo[0]:  # Check if the profile username matches the school username
                        education = School(sInfo[1],
                                           sInfo[2],
                                           sInfo[3])

                        break

            globals.profiles.append(Profile(pInfo[0],
                                            pInfo[1],
                                            pInfo[2],
                                            pInfo[3].replace("_", " "),
                                            pInfo[4],
                                            pInfo[5],
                                            pInfo[6].replace("_", " "),
                                            experience,
                                            education))


def ViewProfile():
    if (globals.currentProfile == None):
        selection = input("Your profile is empty, would you like to fill it out? (y/n) ")
        if (selection == 'y' or selection == 'Y'):
            CreateProfile()
    else:
        print(globals.currentProfile.Print())


def CreateProfile():
    """Process information for a new user profile"""
    validDate = False
    validDegree = False
    print("Creating Profile for ", globals.currentAccount.username)
    firstName = globals.currentAccount.firstname
    lastName = globals.currentAccount.lastname
    title = input("Enter a title for yourself (i.e. \"3rd year Computer Science Student\"): ")
    major = ToPascal(input("Enter your intended major: "))
    schoolName = ToPascal(input("Enter your school's name: "))
    bio = input("Enter a brief description about yourself: ")

    experience = []
    selection = input("Would you like to add any workplace experience? (y/n) ")
    if selection == 'y' or selection == 'Y':
        for i in range(0, 3):
            jobTitle = input("Enter your job title: ")
            employer = input("Enter the name of your employer: ")
            startDate = input("Enter the date you started working there (format YYYY-MM-DD): ")

            while not validDate:
                if ValidateDate(startDate):
                    validDate = True
                else:
                    startDate = input("Incorrect Format for Start date. Try Again (YYYY-MM-DD): ")
            validDate = False
            endDate = input("Enter the date you stopped working there (format YYYY-MM-DD): ")

            while not validDate:
                if ValidateDate(endDate):
                    validDate = True
                else:
                    endDate = input("Incorrect Format for End date. Try Again (YYYY-MM-DD): ")
            location = input("Enter the location of the employer: ")
            description = input("Enter a brief description of your job: ")

            experience.append(
                Experience(jobTitle, employer, date.fromisoformat(startDate), date.fromisoformat(endDate), location,
                           description))
            with open("Experiences.txt", "a+") as file1:
                print("{}".format(globals.currentAccount.username + ' ' + experience[len(experience) - 1].Write()),
                      file=file1)

            selection = input("Would you like to add any more employment history? (y/n) ")
            if selection == 'n' or selection == 'N':
                break
    otherSchool = ToPascal(input("Enter the name of another school you attended: "))
    degree = input("Enter the type of degree you went for (Associate/Bachelor/Master/Doctorate): ")
    while not validDegree:
        if ValidateDegree(degree):
            validDegree = True
        else:
            degree = input("Please enter one of the four degrees (Associate/Bachelor/Master/Doctorate): ")
    years = int(input("Enter the amount of years you attended: "))

    education = School(otherSchool, degree, years)
    with open("Education.txt", "a+") as file2:
        print("{}".format(globals.currentAccount.username + ' ' + education.Write()), file=file2)
    globals.currentProfile = Profile(globals.currentAccount.username, firstName, lastName, title, major, schoolName,
                                     bio, experience, education)
    globals.profiles.append(globals.currentProfile)

    with open("Profiles.txt", "a+") as file3:
        print("{}".format(globals.currentProfile.Write()), file=file3)


def FindProfile(user):
    for p in globals.profiles:
        if p.username == user:
            return p
    return None


def SearchProfiles():
    """Return a list of profiles based on specified lastname, major, or college"""
    result = []
    lastname = input('Enter last name (or leave blank): ')
    major = input('Enter major (or leave blank): ')
    college = input('Enter the school name (or leave blank): ')
    for p in globals.profiles:
        if lastname.upper() in p.lastName.upper() and ToPascal(major).upper() in p.major.upper() and ToPascal(
                college).upper() in p.schoolName.upper():
            result.append(p)

    if len(result) == 0:
        print("No results found.")
    else:
        r = 0;
        while r < len(result):
            print('[' + str(r + 1) + '.]'
                  + result[r].firstName + ' '
                  + result[r].lastName + '\t'
                  + result[r].major + '\t'
                  + result[r].schoolName)

            r = r + 1

        fullName = result[r - 1].firstName + result[r - 1].lastName
        selection = input("Would you like to send a request to any of these people? (y/n) ")
        if selection.upper() == 'Y':
            selection = input(
                'Enter the number of the person you would like to send a request to (or 0 if you wish to exit): ')
            if (int(selection) <= len(result)):
                SendRequest(fullName)
            else:
                while (selection > len(result)):
                    selection = input("Number not on the list, please try again (or 0 to exit): ")
                    SendRequest(fullName)


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
            # Prompt the user to send a friend request
            sendRequestChar = input(f"\nWould you like to send {firstName} a friend request? Press [Y] or [N] ")
            while (sendRequestChar.upper() != 'Y' and sendRequestChar.upper() != 'N'):
                sendRequestChar = input("Please enter [Y] to send a friend request or [N] to exit ")

            # Send Friend Request
            if (sendRequestChar.upper() == 'Y' and globals.loggedIn):
                # Not Written yet
                SendRequest()

            break
    if not found:
        print("\n" + "They are not yet a part of the InCollege system.")

    if found and not globals.loggedIn:
        print("Join your friends today by signing in or creating an account.")


# job functions
def CreateJob():
    """Create a new job posting."""
    if (len(globals.jobs) >= 10):
        print('\n' + 'All permitted job postings have been created, please come back later')
        return
    title = input("Enter the job title: ")
    description = input("Enter a job description: ")
    employer = input("Enter the employer: ")
    location = input("Enter the job location: ")
    salary = input("Enter salary (do not include and non-numerical characters): ")
    while (salary.isnumeric() == False):
        salary = input("Enter salary (do not include and non-numerical characters): ")
    salary = int(salary)
    globals.jobs.append(Job(str(globals.currentAccount.username), title, description, employer, location, salary))
    with open("Jobs.txt", "a+") as file1:
        file1.write(globals.jobs[len(globals.jobs) - 1].PrintWithCreator())  # PrintWithCreator function added in at the last minute
        # print(globals.jobs[len(globals.jobs) - 1].Info(), file=file1)


def DeleteJob(jobNum):
    globals.jobs.remove(globals.jobs[jobNum - 1])
    with open("Jobs.txt", "r") as f:
        lines = f.readlines()
    with open("Jobs.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != globals.jobs[jobNum - 1]:
                f.write(line)


def SaveJob(jobNum):
    globals.savedJobs.append(globals.jobs[jobNum - 1])
    with open("SavedJobs.txt", "w") as saveFile:
        saveFile.write(globals.savedJobs[len(globals.jobs) - 1])


def DisplayJobDetails():
    # display all details for selected job listing
    global selection
    print("Job listing: ", globals.jobs[selection - 1].Print())

    while True:
        apply = input(
            "Enter [A] to apply to this job \n" + "Enter [S] to save this job \n" + "Enter [D] to delete this job \n" + f"Press [{globals.goBack.upper()}] to exit" + '\n')
        apply = apply.lower()
        if (apply == 'a'):
            SubmitApplication()
            return
        elif (selection == 's'):
            SaveJob(selection)
            return
        elif (apply == 'd'):
            DeleteJob(selection)
            return
        elif (apply == globals.goBack):
            return


def DisplayJobs():
    # display job listing titles
    for i in range(len(globals.jobs)):
        print("Job listing", i + 1, ": ", globals.jobs[i].title)

def DisplayUsers():
    for i in range(len(globals.students)):
        print(globals.students[i].username,'\n')
    recipient = input("Enter the username of the account you would like to message:")
    for i in range(len(globals.students)):
        if (globals.students[i].username == recipient):
            text = input('\nEnter the message you would like to send '+ globals.students[i].username + '\n' )
            inbox.SendMessage(globals.currentAccount.username,recipient,text)

def JobMenu():
    # once job titles are displayed, this will allow navigation through jobs and applications
    global selection
    while True:
        DisplayJobs()
        selection = input(
            "\n" + "Enter the number of the job listing you would like to view" + '\n'
            + "Enter [H] to filter out the jobs you have applied to" + '\n'
            + "Enter [N] to filter out the jobs you have NOT applied to" + '\n'
            + "Enter [S] to show the jobs you have had saved" + '\n'
            + f"Press [{globals.goBack.upper()}] to exit" + '\n')
        selection = selection.lower()

        if (selection.isnumeric()):
            selection = int(selection)
            if (selection > 0):
                if (selection <= len(globals.jobs)):
                    DisplayJobDetails()
        elif (selection == 'h'):
            for i in range(len(globals.jobs)):
                for j in range(len(globals.myApplications)):
                    if globals.jobs[i] == globals.myApplications[j].intendedJob:
                        print("You have already applied to job " + str(i) + ".\n")
                        break
        elif (selection == 'n'):
            applied = False
            for i in range(len(globals.jobs)):
                for j in range(len(globals.myApplications)):
                    if globals.jobs[i] == globals.myApplications[j].intendedJob:
                        applied = True
                        break
                if not applied:
                    print("You have not yet applied to job " + str(i) + ".\n")
                applied = False
        elif (selection == 's'):
            for i in range(len(globals.savedJobs)):
                print("Job " + i + " information: " + globals.savedJobs[i])
        elif (selection == globals.goBack):
            return selection


def SubmitApplication():
    validDate = False
    global selection
    while not (validDate):
        gradDate = input("Enter the date you should be graduating (format YYYY-MM-DD): ")
        validDate = ValidateDate(gradDate)
    validDate = False
    while not (validDate):
        startDate = input("Enter the date you can start working (format YYYY-MM-DD): ")
        validDate = ValidateDate(startDate)
    coverletter = input("Enter your cover letter for this job:\n")

    globals.myApplications.append(
        Application(gradDate, startDate, coverletter, globals.jobs[selection - 1], globals.currentAccount.username))
    with open("Applications.txt", "a+") as file1:
        print("{}".format(globals.myApplications[len(globals.myApplications) - 1].Info()), file=file1)
    print("Your application has been submitted!\n")
    return


# main menu options
def CreateAccount():
    """Create a new user account."""
    validUser = False
    validPass = False
    global choice
    if (len(globals.students) >= 10):
        print('\n' + 'All permitted accounts have been created, please come back later')
        return

    # must check if max account #'s is reached
    # bool for whether password is valid

    # take in username
    while (validUser == False):
        inputUser = input("\n" + "Please enter a UNIQUE username without spaces: ")
        validUser = ValidateUser(inputUser)

    # ** this is where we should validate username  (not the same as another username)

    # take in password
    while (validPass == False):
        inputPass = input(
            "Please enter a password (must contain 8 to 12 characters, one capital letter, one digit, and one symbol): ")
        validPass = ValidatePassword(inputPass)
        # below should also confirm password is valid ( minimum of 8 characters), (maximum of 12 characters), (at least one capital letter), (one digit), (one non-alpha character)

    # take in first name
    inputFirstName = input("Please enter your first name: ")

    # take in last name
    inputLastName = input("Please enter your last name: ")

    # once username and password are deemed valid, place new user in .txt file and array
    globals.students.append(User(inputUser,
                                 inputPass,
                                 inputFirstName,
                                 inputLastName,
                                 emailAlerts=True,
                                 textAlerts=True,
                                 targetedAdvertising=True,
                                 language="English"))
    with open("Logins.txt", "a+") as text_file:
        print("{}".format(globals.students[len(globals.students) - 1].Print()), file=text_file)
    CreateFriendsList(inputUser)
    print('Account successfully created!')

    ## logins.truncate(0)   this is the erase file function in case accounts must be rewritten
def LoginToAccount():
    """Attempt to log the user into an account."""
    global choice
    # global loggedIn

    while True:
        # take in username
        inputUser = input("\n" + "Please enter a username: ")

        # take in password
        inputPass = input("Please enter a password: ")

        # looks through each account, sends it straight to CheckLogin() and when one returns true it will set as current Account and inform user login was a success
        for account in globals.students:
            if (account.CheckLogin(inputUser, inputPass)):
                print('You have successfully logged in')
                choice = 'ah'
                globals.loggedIn = True
                globals.currentAccount = account
                globals.currentProfile = FindProfile(globals.currentAccount.username)
                LoadMyApplications()
                return

        # Display an error message if the login fails
        # Allow the user to try again or go back
        while True:
            choice = input(
                '\n' + 'Incorrect username / password.' + '\n\n' \
                                                          'Press [L] to try again.' + '\n' \
                                                                                      f'Press [{globals.goBack.upper()}] to return to the previous menu.' + '\n')
            choice = choice.lower()
            if choice == globals.goBack:
                return
            elif choice == 'l':
                break
            else:
                continue


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
        print(f"Press [{globals.goBack.upper()}] to return to the previous menu")

        selection = input("")
        selection = selection.lower()
        if selection in skills.keys():
            print("Under construction" + "\n")
        elif selection == globals.goBack:
            break
        elif selection not in skills.keys():
            continue
            # menus

def ShowLoggedOutMenu():
    """Present menu options for when the user is logged out."""
    while True:
        selection = input(
            "\n" + "Would you like to sign in or create an account?" + '\n' \
            + "Press [L] to login" + '\n' \
            + "Press [C] to create an account" + '\n' \
            + "Press [F] to find someone" + '\n' \
            + "Press [W] to watch a video" + '\n' \
            + "Press [U] for Useful Links" + '\n' \
            + "Press [I] to show InCollege important links" + '\n' \
            + f"Press [{globals.goBack.upper()}] to quit" + '\n')
        selection = selection.lower()

        # this could probs be a switch so I will SWITCH it to that haha fml
        if (selection == 'c'):
            CreateAccount()
        elif (selection == 'l'):
            LoginToAccount()
            return selection
        elif (selection == 'f'):
            FindContact()
        elif (selection == 'w'):
            print("Video is now playing", flush=True)
            time.sleep(20)
            print("Video ending...", flush=True)
            time.sleep(3)
        elif (selection == 'u'):
            ShowUsefulLinks()
        elif (selection == 'i'):
            ImportantLinks.ShowMenu()
       
        elif (selection == globals.goBack):  # Break out of the inner loop
            return selection


def FriendMenu(friend):
    """Displays options for selected friend from list, only displays profiles from those who have it"""
    prof_found = FindProfile(friend)
    if prof_found != None:
        print(f"Press [P] to view {friend}\'s profile")
    selection = input(f"Press [R] to remove {friend} from your friends list\nPress [Q] to exit\nMake a selection: ")

    if selection.lower() == 'p' and prof_found != None:
        ViewUserProfile(friend)
    elif selection.lower() == 'r':
        selection = input(f"Are you sure you want to delete {friend} from your list? (y/n)")
        if selection.lower() == 'y':
            DeleteFriends(friend)
    else:
        pass


def ShowLoggedInMenu():
    """Present menu options for when the user is logged in."""
    while True:
        selection = input(
            "\n" + "Press [R] to view your profile" + '\n' \
            + "Press [F] to find someone" + '\n' \
            + "Press [S] to search profiles" + '\n' \
            + "Press [J] to look for a job" + '\n' \
            + "Press [P] to post a job" + '\n' \
            + "Press [L] to learn a new skill" + '\n' \
            + "Press [U] for Useful Links" + '\n' \
            + "Press [I] to show InCollege important links" + '\n' \
            + "Press [V] to view friends list" + '\n' \
            + "Press [E] to check your pending friend requests." + '\n' \
            + "Press [M] to open the messaging menu" + '\n' \
            + f"Press [{globals.goBack.upper()}] to log out" + '\n')
        selection = selection.lower()

        if (selection == 'r'):
            ViewProfile()
        elif (selection == 'f'):
            FindContact()
        elif (selection == 's'):
            SearchProfiles()
        elif (selection == 'j'):
            JobMenu()
        elif (selection == 'l'):
            LearnSkill()
        elif (selection == 'p'):
            CreateJob()
        elif (selection == 'i'):
            ImportantLinks.ShowMenu()
        elif (selection == 'u'):
            ShowUsefulLinks()
        elif (selection == 'v'):  # View Friends List
            ViewFriendsList()
        elif (selection == 'e'):
            ViewRequests()
        elif (selection == 'm'):
           MessageingMenu()
        elif (selection == globals.goBack):
            globals.loggedIn = False
            globals.myApplications.clear()
            return selection

def MessageingMenu():
    global choice
    while True:
        choice = input(
            "\n" + "Press [V] to view inbox" + '\n' \
            + "Press [S] send message" + '\n' \
            + f"Press [{globals.goBack.upper()}] to return to the previous menu" + '\n')
        choice = choice.lower()

        if (choice == 'v'):  # Help Center
            inbox.ShowPersonalInbox(str(globals.currentAccount.username))
        elif (choice == 's'):  # Developers
            DisplayUsers()
        elif (choice == globals.goBack):  # Go back to Useful Links
            choice == ''
            return

        quitLogic()

def ShowUsefulLinks():
    global choice
    while True:
        choice = input(
            "\n" + "Press [G] for General links" + '\n' \
            + "Press [B] to Browse InCollege" + '\n' \
            + "Press [U] for Business Solutions" + '\n' \
            + "Press [D] for Directories" + '\n' \
            + f"Press [{globals.goBack.upper()}] to return to the previous menu" + '\n')
        choice = choice.lower()

        if (choice == 'g'):  # General Links
            ShowGeneralLinks()
        elif (choice == 'b'):  # Browse InCollege
            ShowUnderConstruction()
        elif (choice == 'u'):  # Business Solutions
            ShowUnderConstruction()
        elif (choice == 'd'):  # Directories # May need changed
            ShowUnderConstruction()
        elif (choice == globals.goBack):  # Go back to the previous menu
            choice = ''
            return
        # Go back to sign up page (second break) (need to go back twice)
        if (choice == 's'):
            return

    quitLogic()


def ShowGeneralLinks():
    global choice
    while True:
        choice = input(
            "\n" + "Press [S] to Sign up" + '\n' \
            + "Press [H] for the Help Center" + '\n' \
            + "Press [A] for About" + '\n' \
            + "Press [P] for Press" + '\n' \
            + "Press [B] for Blog" + '\n' \
            + "Press [C] for Careers" + '\n' \
            + "Press [D] for Developers" + '\n' \
            + f"Press [{globals.goBack.upper()}] to return to the previous menu" + '\n')
        choice = choice.lower()

        if (choice == 'h'):  # Help Center
            print("\nWe're here to help", flush=True)
        elif (choice == 'a'):  # About
            print("\nIn College: Welcome to In College, " +
                  "the world's largest college student network with many users " +
                  "in many countries and territories worldwide", flush=True)
        elif (choice == 'p'):  # Press
            print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports", flush=True)
        elif (choice == 'b'):  # Blog
            ShowUnderConstruction()
        elif (choice == 'c'):  # Careers
            ShowUnderConstruction()
        elif (choice == 'd'):  # Developers
            ShowUnderConstruction()
        elif (choice == globals.goBack):  # Go back to Useful Links
            choice == ''
            return

        # Go back to sign up page (first break) (need to go back twice) (Don't reset choice)
        if (choice == 's'):
            return

        quitLogic()


def ShowUnderConstruction():
    print("\n" + "Under construction")


def quitLogic():
    global choice
    while (choice != 'q'):
        choice = input(f"\nPress [{globals.goBack.upper()}] to return to the previous menu:\n")


# include function to call from CreateAccount()  that would create account (change user and pass from "NULL") then add info to some .txt file for permanent storage
# include function that upon starting InCollege app would open .txt file and create already existing accounts / add them to array
# need function to check if any account spots are left
# def FreeSpace ():
def mainMenu():
    """Show the main menus to the user."""
    # create array of size max # of students

    global logins
    global choice
    global friendsLists
    global requests

    globals.currentProfile = None
    logins = open('Logins.txt', 'a+')
    choice = 'd'
    friendsLists = []
    requests = []

    LoadAccounts()
    # this is where we at first should intercept and load text file accounts
    SuccessStory()
    LoadProfiles()
    LoadFriendsList()
    LoadRequests()
    LoadJobs()
    LoadMessages()
    while True:  # Logged in and logged out menu loop
        while not globals.loggedIn:
            choice = ShowLoggedOutMenu()
            if (choice == globals.goBack):  # Break out of the logged out menu
                break
        if (choice == globals.goBack):  # Break out of the main menu to exit the program
            break

        while globals.loggedIn:
            FindNotification()
            choice = ShowLoggedInMenu()
            if (choice == globals.goBack):  # Break out and go back to the logged out menu
                break


if __name__ == "__main__":
    globals.Initialize()
    mainMenu()