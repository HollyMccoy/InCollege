# Main PyTest program for InCollege unit tests

from _Tests import test_MainFiles  # Main directory files
from _Tests import test_ImportantLinksFiles  # "Important links" submenu files
from _Tests import test_Validation  # Validation functions
from _Tests import test_Friends  # Friend list functionality
from _Tests import test_Requests  # Friend request functionality
from _Tests import test_NotificationFiles  # "Notications" submenu files

#Making sure all the main files are present
mainTest = test_MainFiles.TestMainFiles

def test_Files():
    mainTest.test_EducationFile(mainTest)
    mainTest.test_ExperiencesFile(mainTest)
    mainTest.test_FriendsFile(mainTest)
    mainTest.test_JobsFile(mainTest)
    mainTest.test_LoginsFile(mainTest)
    mainTest.test_MessagesFile(mainTest)
    mainTest.test_ProfilesFile(mainTest)
    mainTest.test_RequestsFile(mainTest)
    mainTest.test_SkillsFile(mainTest)
    mainTest.test_SuccessStoryFile(mainTest)


