# Unit tests for API output functionality

from os import path

pathDir = "docs\\API\\output\\"

jobsFile = pathDir + "MyCollege_jobs.txt"
profilesFile = pathDir + "MyCollege_profiles.txt"
userFile = pathDir + "MyCollege_users.txt"
trainingFile = pathDir + "MyCollege_training.txt"
appliedJobsFile = pathDir + "MyCollege_appliedJobs.txt"
savedJobsFile = pathDir + "MyCollege_savedJobs.txt"


class TestFilesExist:
    """Check if the API output files exist."""
    def test_JobsFile(self):
        assert path.exists(jobsFile)

    def test_ProfilesFile(self):
        assert path.exists(profilesFile)

    def test_UserFile(self):
        assert path.exists(userFile)

    def test_TrainingFile(self):
        assert path.exists(trainingFile)

    def test_AppliedJobsFile(self):
        assert path.exists(appliedJobsFile)

    def test_SavedJobsFile(self):
        assert path.exists(savedJobsFile)


class TestFileFormat:
    """Check for the expected formats of the API output files."""
    def test_JobsFile(self):
        with open(jobsFile) as file:
            valid = True
            title = None
            description = None
            employer = None
            location = None
            salary = None
            sep = "====="  # Job separation string

            lines = file.read().splitlines()
            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                for lineNum, lineText in enumerate(lines, 1):  # Number each line starting at 1
                    if lineText == '':  # Check for blank lines
                        valid = False
                        break
                    if lineNum % 6 == 1:  # Title
                        try:
                            title = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 6 == 2:  # Description
                        try:
                            description = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 6 == 3:  # Employer
                        try:
                            employer = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 6 == 4:  # Location
                        try:
                            location = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 6 == 5:  # Salary
                        try:
                            salary = int(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 6 == 0:  # Job separation string
                        if lineText != sep:
                            valid = False
                            break
                assert valid


    def test_ProfilesFile(self):
        with open(profilesFile) as file:
            valid = True
            username = None
            title = None
            major = None
            university = None
            about = None
            experience = None
            education = None
            sep = "====="  # Job separation string

            lines = file.read().splitlines()
            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                for lineNum, lineText in enumerate(lines, 1):  # Number each line starting at 1
                    if lineText == '':  # Check for blank lines
                        valid = False
                        break
                    if lineNum % 8 == 1:  # Username
                        try:
                            username = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 2:  # Title
                        try:
                            title = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 3:  # Major
                        try:
                            major = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 4:  # University
                        try:
                            university = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 5:  # About
                        try:
                            about = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 6:  # Experience
                        try:
                            experience = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 7:  # Education
                        try:
                            education = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 8 == 0:  # Job separation string
                        if lineText != sep:
                            valid = False
                            break
                assert valid


    def test_UserFile(self):
        with open(userFile) as file:
            valid = True
            username = None
            accountType = None
            sep = "====="  # Job separation string

            lines = file.read().splitlines()
            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                accounts = list()
                for line in lines:
                    accounts.append(line.split())
                for account in accounts:
                    try:
                        username = str(account[0])
                        accountType = str(account[1])
                        if (accountType != "standard" and accountType != "plus"):
                            valid = False
                    except:
                        valid = False
                        break
                assert valid


    def test_TrainingFile(self):
        with open(trainingFile) as file:
            valid = True
            sep = "====="  # Job separation string

            temp = file.read().splitlines()

            # Split each string into separate list items
            lines = list()
            [lines.append(line.split(',')) for line in temp]

            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                for line in lines:
                    if len(line) == 1:  # Check for isolated usernames
                        valid = False
                    for param in line:
                        if param == "":  # Check for blank parameters
                            valid = False
                        try:
                            str(param)
                        except:
                            valid = False
                            break
                assert valid


    def test_AppliedJobsFile(self):
        with open(appliedJobsFile) as file:
            valid = True
            title = None
            username = None
            appReason = None
            sep = "====="  # Job separation string

            lines = file.read().splitlines()
            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                for lineNum, lineText in enumerate(lines, 1):  # Number each line starting at 1
                    if lineText == '':  # Check for blank lines
                        valid = False
                        break
                    if lineNum % 4 == 1:  # Title
                        try:
                            title = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 4 == 2:  # Username
                        try:
                            username = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 4 == 3:  # Reason for applying
                        try:
                            appReason = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 4 == 0:  # Job separation string
                        if lineText != sep:
                            valid = False
                            break
                assert valid


    def test_SavedJobsFile(self):
        with open(savedJobsFile) as file:
            valid = True
            username = None
            title = None
            sep = "====="  # Job separation string

            lines = file.read().splitlines()
            if len(lines) == 0:  # Return true if file is empty
                return True
            else:  # Check for expected parameters
                for lineNum, lineText in enumerate(lines, 1):  # Number each line starting at 1
                    if lineText == '':  # Check for blank lines
                        valid = False
                        break
                    if lineNum % 3 == 1:  # Username
                        try:
                            title = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 3 == 2:  # Title
                        try:
                            username = str(lineText)
                        except:
                            valid = False
                            break
                    elif lineNum % 3 == 0:  # Job separation string
                        if lineText != sep:
                            valid = False
                            break
                assert valid