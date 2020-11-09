class Profile:
    def __init__(self,
        username,
        firstName,
        lastName,
        title,
        major,
        schoolName,
        bio,
        experience,
        education):

        self.experience = []

        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.title = title
        self.major = major
        self.schoolName = schoolName
        self.bio = bio
        self.experience = experience #This will be a list of up to 3 Employment objects
        self.education = education

    def Print(self):
        history = "Employment History\n"
        for h in self.experience:
            history += ("----------------------------------------\n"
            + h.Print()
            + "----------------------------------------\n")
        return("----------------------------------------\n"
        + self.firstName + " " + self.lastName + "\n"
        + self.title + "\n----------------------------------------\n"
        + "School: " + self.schoolName + "\n"
        + "About: " + self.bio + "\n\n"
        + history + "\n"
        + self.education.Print())

    def Write(self):
        return(self.username + ' ' + self.firstName + ' ' + self.lastName + ' ' + self.title.replace(" ", "_") + ' ' + self.major + ' ' + self.schoolName + ' ' + self.bio.replace(" ", "_") + "\n")