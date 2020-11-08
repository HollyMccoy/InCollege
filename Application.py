import locale
import datetime


class Application:
    def __init__(self, gradDate, startDate, coverLetter, intendedJob, username):  # constructor
        self.gradDate = gradDate
        self.startDate = startDate
        self.coverLetter = coverLetter
        self.intendedJob = intendedJob
        self.username = username
    # a title, a description, the employer, a location, and a salary

    def Info(self):
        locale.setlocale(locale.LC_ALL, '')
        return (self.username + '\n'
            +  self.intendedJob.Info()  + '\n'
            +  self.gradDate  + '\n'
            +  self.startDate + '\n'
            + self.coverLetter.replace("_", " "))