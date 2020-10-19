# Global variables and functions for unit test files

def checkParamLength(fileName, numParams):
    """Check for a specified number of file parameters"""
    with open(fileName) as file:
        while True:
            params = file.readline().split()
            if not params:  # Exit if at end-of-file
                break
            elif len(params) == 0:  # Skip blank lines
                continue
            elif len(params) != numParams:
                print("Incorrect number of parameters found in " + fileName)
            return len(params) == numParams


def checkIfEmpty(fileName):
    """Check if a specified file is empty"""
    with open(fileName) as file:
        while True:
            line = file.readline()
            if not line:
                return False
            elif line == "\n":
                return False
            else:
                return True
