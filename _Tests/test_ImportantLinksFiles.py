# Unit tests for "important links" subdirectory files
from os import path

fileDir = "docs\\ImportantLinks\\"


class TestImportantLinksFiles:
    '''Check for files used by the "important links" submenus.'''
    def test_ImportantLinksPath(self):
        assert path.exists(fileDir)

    def test_AboutFile(self):
        assert path.exists(fileDir + "About.txt")

    def test_AccessibilityFile(self):
        assert path.exists(fileDir + "Accessibility.txt")

    def test_BrandPolicyFile(self):
        assert path.exists(fileDir + "BrandPolicy.txt")

    def test_CookiePolicyFile(self):
        assert path.exists(fileDir + "CookiePolicy.txt")

    def test_CopyrightNoticeFile(self):
        assert path.exists(fileDir + "CopyrightNotice.txt")

    def test_CopyrightPolicyFile(self):
        assert path.exists(fileDir + "CopyrightPolicy.txt")

    def test_PrivacyPolicyFile(self):
        assert path.exists(fileDir + "PrivacyPolicy.txt")

    def test_UserAgreementFile(self):
        assert path.exists(fileDir + "UserAgreement.txt")
