# Unit tests for "Notifications" subdirectory files
from os import path

fileDir = "docs\\Notifications\\"


class TestNotificationFiles:
    '''Check for files used by the "important links" submenus.'''
    def test_ImportantLinksPath(self):
        assert path.exists(fileDir)

    def test_ApplyTimesFile(self):
        assert path.exists(fileDir + "ApplyTimes.txt")

    def test_DeletedJobsFile(self):
        assert path.exists(fileDir + "DeletedJobs.txt")

    def test_NewJobsFile(self):
        assert path.exists(fileDir + "NewJobNotifications.txt")