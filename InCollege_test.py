from InCollege import ValidatePassword, ValidateDate, ValidateDegree

class TestValidatePassword:
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
    def test_ValidateDegree(self):
        assert ValidatePassword("Other Option that should be false") == False
    
    def test_ValidateDegreeIncorrected(self):
        assert ValidatePassword("Example") == False

    def test_ValidateDegreeAssoiciate(self):
        assert ValidatePassword("Associate") == True

    def test_ValidateDegreeBachelor(self):
        assert ValidatePassword("Bachelor") == True

    def test_ValidateDegreeMaster(self):
        assert ValidatePassword("Master") == True

    def test_ValidateDegreeDoctorate(self):
        assert ValidatePassword("Doctorate") == True



class TestValidateDate:
    
    def test_ValidateDateInFormat(self):
        assert ValidatePassword("2020-12-10") == True

    def test_ValidateDateNotInFormat(self):
        assert ValidatePassword("2020-march-23") == False
