# Main PyTest program for InCollege unit tests

from _Tests import test_MainFiles  # Main directory files
from _Tests import test_ImportantLinksFiles  # "Important links" submenu files
from _Tests import test_Validation  # Validation functions
from _Tests import test_Friends  # Friend list functionality
from _Tests import test_Requests  # Friend request functionality
import InCollege
import globals

#Making sure all the main files are present
mainTest = test_MainFiles.TestMainFiles
passwordTest = test_Validation.TestValidatePassword
def test_Files():
    mainTest.test_EducationFile(mainTest)
    mainTest.test_ExperiencesFile(mainTest)
    mainTest.test_FriendsFile(mainTest)
    mainTest.test_JobsFile(mainTest)
    mainTest.test_LoginsFile(mainTest)
    mainTest.test_ProfilesFile(mainTest)
    mainTest.test_RequestsFile(mainTest)
    mainTest.test_SkillsFile(mainTest)
    mainTest.test_SuccessStoryFile(mainTest)

def test_InCollegeJobs():
    globals.Initialize()
    global logins
    global choice
    global friendsLists
    global requests
    globals.currentProfile = None
    logins = open('Logins.txt', 'a+')
    choice = 'd'
    friendsLists = []
    requests = []
    InCollege.LoadJobs()
