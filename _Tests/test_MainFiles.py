# Unit tests for main directory files

from os import path
from _Tests.testGlobals import checkIfEmpty
from _Tests.testGlobals import checkParamLength

educationFile = "Education.txt"
experiencesFile = "Experiences.txt"
friendsFile = "Friends.txt"
jobsFile = "Jobs.txt"
loginsFile = "Logins.txt"
messagesFile = "Messages.txt"
profilesFile = "Profiles.txt"
requestsFile = "Requests.txt"
skillsFile = "Skills.txt"
successStoryFile = "SuccessStory.txt"

class TestMainFiles:
    """Check for files in the root directory."""
    def test_EducationFile(self):
        assert path.exists(educationFile)

    def test_ExperiencesFile(self):
        assert path.exists(experiencesFile)

    def test_FriendsFile(self):
        assert path.exists(friendsFile)

    def test_JobsFile(self):
        assert path.exists(jobsFile)

    def test_LoginsFile(self):
        assert path.exists(loginsFile)

    def test_MessagesFile(self):
        assert path.exists(messagesFile)

    def test_ProfilesFile(self):
        assert path.exists(profilesFile)

    def test_RequestsFile(self):
        assert path.exists(requestsFile)

    def test_SkillsFile(self):
        assert path.exists(skillsFile)

    def test_SuccessStoryFile(self):
        assert path.exists(successStoryFile)


class TestMainFilesParameters:
    """Check each input file for the appropriate number of file parameters."""
    def test_EducationFile(self):
        if checkIfEmpty(educationFile):
            assert True
        else:
            assert checkParamLength(educationFile, 4)

    def test_ExperiencesFile(self):
        if checkIfEmpty(experiencesFile):
            assert True
        else:
            assert checkParamLength(experiencesFile, 7)

    def test_JobsFile(self):
        if checkIfEmpty(jobsFile):
            assert True
        else:
            assert checkParamLength(jobsFile, 5)

    def test_LoginsFile(self):
        if checkIfEmpty(loginsFile):
            assert True
        else:
            assert checkParamLength(loginsFile, 9)

    def test_ProfilesFile(self):
        if checkIfEmpty(profilesFile):
            assert True
        else:
            assert checkParamLength("Profiles.txt", 7)