import locale
import datetime
class Job:
    def __init__ (self, title, description, employer, location, salary ):     #constructor
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary

    # a title, a description, the employer, a location, and a salary
    def Info(self):
        return  self.title + ' \n' + self.description + ' \n' + self.employer  +' \n' +  self.location  +' \n' +   str(self.salary)

    def Print(self):
        locale.setlocale(locale.LC_ALL, '')
        return ' ' + self.title + ' ' + self.description + ' ' + self.employer + ' ' + self.location + ' ' +  str(self.salary) + '\n'
        
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
        return (self.title.replace(" ", "_") + ' ' + self.employer.replace(" ", "_") + ' ' + self.start_date.isoformat() + ' ' + self.end_date.isoformat() + ' ' + self.location.replace(" ", "_") + ' ' + self.description.replace(" ", "_") + '\n')