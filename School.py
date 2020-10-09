class School:
    def __init__(self,name,degree,years):
        self.name = name
        self.degree = degree
        self.years = years
    
    def Print(self):
        return ("Education\n----------------------------------------\n" 
        + "School: " + self.name + "\n"
        + "Degree: " + self.degree + "\n"
        + "Years attended: " + str(self.years) + "\n----------------------------------------\n")
        
    def Write(self):
        return (self.name + ' ' + self.degree + ' ' + str(self.years) + '\n')