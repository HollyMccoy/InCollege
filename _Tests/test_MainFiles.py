# Unit tests for main directory files

from os import path
from _Tests.testGlobals import checkParamLength

class TestMainFiles:
    """Check for files in the root directory."""
    def test_EducationFile(self):
        assert path.exists("Education.txt")

    def test_ExperiencesFile(self):
        assert path.exists("Experiences.txt")

    def test_FriendsFile(self):
        assert path.exists("Friends.txt")

    def test_JobsFile(self):
        assert path.exists("Jobs.txt")

    def test_LoginsFile(self):
        assert path.exists("Logins.txt")

    def test_ProfilesFile(self):
        assert path.exists("Profiles.txt")

    def test_SkillsFile(self):
        assert path.exists("Skills.txt")

    def test_SuccessStoryFile(self):
        assert path.exists("SuccessStory.txt")


class TestMainFilesContent:
    """Check each input file for the appropriate number of file parameters."""

    # Ignore the following files due to having a variable number of parameters:
    '''
    Friends.txt
    Skills.txt
    SuccessStory.txt
    '''

    def test_EducationFile(self):
        checkParamLength("Education.txt", 4)

    def test_ExperiencesFile(self):
        checkParamLength("Experiences.txt", 7)

    def test_JobsFile(self):
        checkParamLength("Jobs.txt", 5)

    def test_LoginsFile(self):
        checkParamLength("Logins.txt", 8)

    def test_ProfilesFile(self):
        checkParamLength("Profiles.txt", 7)
