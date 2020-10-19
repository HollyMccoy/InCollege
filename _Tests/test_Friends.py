# Unit tests for friends list functionality


class TestFriendsListFile:
    """Check for correct parameters within the friends list file."""

    # Constructors do not work with PyTest, so we must read the friends list file for each function
    """
    def __init__(self):
        self.friendsLists = []
        with open("Friends.txt", "r") as friendsListFile:
            while True:
                friendsList = friendsListFile.readline()
                if friendsList:
                    friendsList = friendsList.split()
                    self.friendsLists.append(friendsList)
                else:
                    break
    """


    def test_ObsoleteUser(self):
        """Check for user accounts that no longer exist."""
        # Read in the friends list file
        friendsLists = []
        with open("Friends.txt", "r") as friendsListFile:
            while True:
                friendsList = friendsListFile.readline()
                if friendsList:
                    friendsList = friendsList.split()
                    friendsLists.append(friendsList)
                else:
                    break

        # Read in all accounts from the logins file
        userAccounts = []
        with open("Logins.txt", "r") as loginFile:
            while True:
                userAccount = loginFile.readline()
                if userAccount:
                    userAccount = userAccount.split().pop(0)
                    userAccounts.append(userAccount)
                else:
                    break

        # Check for friended accounts that are not in the login file
        obsoleteUser = False
        for friendsList in friendsLists:
            for friend in friendsList:
                if friend not in userAccounts:
                    obsoleteUser = True
                    break
        assert not obsoleteUser


    def test_DuplicateUser(self):
        """Check for duplicate user accounts."""
        # Read in the friends list file
        friendsLists = []
        with open("Friends.txt", "r") as friendsListFile:
            while True:
                friendsList = friendsListFile.readline()
                if friendsList:
                    friendsList = friendsList.split()
                    friendsLists.append(friendsList)
                else:
                    break

        # Check for duplicate users
        uniqueUsers = True
        uniqueUserList = []
        for friendsList in friendsLists:
            if friendsList[0] not in uniqueUserList:
                uniqueUserList.append(friendsList[0])
            else:
                uniqueUsers = False
                break
        assert uniqueUsers


    def test_DuplicateFriend(self):
        """Check for duplicate user friends."""
        # Read in the friends list file
        friendsLists = []
        with open("Friends.txt", "r") as friendsListFile:
            while True:
                friendsList = friendsListFile.readline()
                if friendsList:
                    friendsList = friendsList.split()
                    friendsLists.append(friendsList)
                else:
                    break

        # Check for duplicate friends for each user
        uniqueFriends = True
        for friendsList in friendsLists:
            for friend in friendsList:
                if friendsList.count(friend) > 1:
                    uniqueFriends = False
                    break
        assert uniqueFriends
