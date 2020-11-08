import locale
import datetime
class Job:
    #def __init__ (self, title, description, employer, location, salary ):     #constructor
    def __init__ (self, creator, title, description, employer, location, salary ):     #constructor
        self.creator = creator
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary

    # a title, a description, the employer, a location, and a salary
    def Info(self):
        return self.title + ' \n' + self.description + ' \n' + self.employer  +' \n' +  self.location  +' \n' +   str(self.salary)

    def PrintWithCreator(self):  # Print job info including the creator of the job; this function was added in at the last minute, so change it if needed
        locale.setlocale(locale.LC_ALL, '')
        return self.creator + ' ' + self.title + ' ' + self.description + ' ' + self.employer + ' ' + self.location + ' ' +  str(self.salary) + '\n'

    def Print(self):  # Print job info excluding the creator of the job
        locale.setlocale(locale.LC_ALL, '')
        return ' ' + self.title + ' ' + self.description + ' ' + self.employer + ' ' + self.location + ' ' +  str(self.salary) + '\n'

    def DisplayListing(self):  # Print out job info in a user-readable format
        print(f"Title:       {self.title.replace('_', ' ')}" + "\n"
            + f"Description: {self.description.replace('_', ' ')}" + "\n"
            + f"Employer:    {self.employer.replace('_', ' ')}" + "\n"
            + f"Location:    {self.location.replace('_', ' ')}" + "\n"
            + f"Salary:      {str(self.salary)}" + "\n")


class Experience:
    def __init__ (self,
        title,
        employer,
        start_date,
        end_date,
        location,
        description):

        self.title = title;
        self.employer = employer;
        self.start_date = start_date;
        self.end_date = end_date;
        self.location = location;
        self.description = description;

    def Print(self):
        return ("Title: " + self.title + "\n"
        + "Employer: " + self.employer + "\n"
        + "Start Date: " + self.start_date.isoformat() + "\n"
        + "End Date: " + self.end_date.isoformat() + "\n"
        + "Location: " + self.location + "\n"
        + "Description: " + self.description + "\n")

    def Write(self):
        return (self.title.replace(" ", "_") + ' '
        + self.employer.replace(" ", "_") + ' '
        + self.start_date.isoformat() + ' '
        + self.end_date.isoformat() + ' '
        + self.location.replace(" ", "_") + ' '
        + self.description.replace(" ", "_") + '\n')
