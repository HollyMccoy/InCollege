# Unit tests for main directory files

from os import path
from _Tests.testGlobals import checkIfEmpty
from _Tests.testGlobals import checkParamLength


class TestMainFiles:
    """Check for files in the root directory."""
    def test_ApplicationsFile(self):
        assert path.exists("Applications.txt")

    def test_CompletedCoursesFile(self):
        assert path.exists("CompletedCourses.txt")

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

    def test_MessagesFile(self):
        assert path.exists("Messages.txt")

    def test_NewUsersFile(self):
        assert path.exists("NewUsers.txt")

    def test_ProfilesFile(self):
        assert path.exists("Profiles.txt")

    def test_RequestsFile(self):
        assert path.exists("Requests.txt")

    def test_SavedJobsFile(self):
        assert path.exists("SavedJobs.txt")

    def test_SkillsFile(self):
        assert path.exists("Skills.txt")

    def test_SuccessStoryFile(self):
        assert path.exists("SuccessStory.txt")


class TestMainFilesContent:
    """Check each input file for the appropriate number of file parameters."""
    def test_EducationFile(self):
        assert checkParamLength("Education.txt", 4)

    def test_ExperiencesFile(self):
        assert checkParamLength("Experiences.txt", 7)

    def test_FriendsFile(self):
        assert checkIfEmpty("Friends.txt")

    def test_JobsFile(self):
        assert checkParamLength("Jobs.txt", 5)

    def test_LoginsFile(self):
        assert checkParamLength("Logins.txt", 9)

    def test_ProfilesFile(self):
        assert checkParamLength("Profiles.txt", 7)

    def test_SkillsFile(self):
        assert checkIfEmpty("Skills.txt")

    def test_SuccessStoryFile(self):
        assert checkIfEmpty("SuccessStory.txt")
