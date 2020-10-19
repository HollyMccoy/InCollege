# Unit tests for validation functions
from InCollege import ValidatePassword, ValidateDegree, ValidateDate


class TestValidatePassword:
    """Test the password criteria for new user accounts."""
    def test_ValidatePasswordTooShort(self):
        assert ValidatePassword("example") == False

    def test_ValidatePasswordTooLong(self):
        assert ValidatePassword("example123456") == False

    def test_ValidatePasswordNoAlphanum(self):
        assert ValidatePassword("Example12") == False

    def test_ValidatePasswordNoCapitalLetter(self):
        assert ValidatePassword("example12") == False

    def test_ValidatePasswordNoNumber(self):
        assert ValidatePassword("exampleee") == False

    def test_ValidatePasswordHappyPath(self):
        assert ValidatePassword("Example1!") == True


class TestValidateDegree:
    """Test the expected degree function inputs."""
    def test_ValidateDegree(self):
        assert ValidateDegree("Other Option that should be false") == False

    def test_ValidateDegreeIncorrected(self):
        assert ValidateDegree("Example") == False

    def test_ValidateDegreeAssoiciate(self):
        assert ValidateDegree("Associate") == True

    def test_ValidateDegreeBachelor(self):
        assert ValidateDegree("Bachelor") == True

    def test_ValidateDegreeMaster(self):
        assert ValidateDegree("Master") == True

    def test_ValidateDegreeDoctorate(self):
        assert ValidateDegree("Doctorate") == True


class TestValidateDate:
    """Test the expected date formats."""
    def test_ValidateDateInFormat(self):
        assert ValidateDate("2020-12-10") == True

    def test_ValidateDateNotInFormat(self):
        assert ValidateDate("2020-march-23") == False
