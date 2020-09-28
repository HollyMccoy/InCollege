import locale
class Job:
    def __init__ (self, title, description, employer, location, salary ):     #constructor
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary

    # a title, a description, the employer, a location, and a salary

    def Print(self):
        locale.setlocale(locale.LC_ALL, '')
        return self.title + ' ' + self.description + ' ' + self.employer + ' ' + self.location + ' ' + locale.currency( self.salary )