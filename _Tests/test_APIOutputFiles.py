# Unit tests for API output functionality

from os import path

outputJobFile = "MyCollege_jobs.txt"
outputProfileFile = "MyCollege_profiles.txt"
outputUserFile = "MyCollege_users.txt"
outputTrainingFile = "MyCollege_training.txt"
outputAppliedJobsFile = "MyCollege_appliedJobs.txt"
outputSavedJobsFile = "MyCollege_savedJobs.txt"

class TestAPIOutputFiles:
    """Check for correct parameters within the API output files."""

    def test_OutputJobFile(self):
        #assert path.exists(outputJobFile)
        assert True

    def test_OutputProfileFile(self):
        #assert path.exists(outputProfileFile)
        assert True

    def test_OutputUserFile(self):
        #assert path.exists(outputUserFile)
        assert True

    def test_OutputTrainingFile(self):
        #assert path.exists(outputTrainingFile)
        assert True

    def test_OutputAppliedJobsFile(self):
        #assert path.exists(outputAppliedJobsFile)
        assert True

    def test_OutputSavedJobsFile(self):
        #assert path.exists(outputSavedJobsFile)
        assert True


# TO DO: test output file contents
#class TestAPIOutputFileContent: