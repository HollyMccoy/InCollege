from InCollege import ValidatePassword

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