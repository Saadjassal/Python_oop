#Topic: Inheritance

# Base class
class Employee:
    company = "software Ltd"  # Class variable shared by all

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: Rs.{self.salary}, Company: {Employee.company}")


# Single inheritance
class Developer(Employee):
    def __init__(self, name, salary, language):
        # Call base Employee constructor
        Employee.__init__(self, name, salary)
        self.language = language

    def show_info(self):
        print(f"Developer: {self.name}, Language: {self.language}, Salary: Rs.{self.salary}")


# Single inheritance
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        # Call base Employee constructor
        Employee.__init__(self, name, salary)
        self.team_size = team_size

    def show_info(self):
        print(f"Manager: {self.name}, Team Size: {self.team_size}, Salary: Rs.{self.salary}")


# Multiple inheritance
class TechLead(Developer, Manager):
    def __init__(self, name, salary, language, team_size):
        Developer.__init__(self, name, salary, language)
        Manager.__init__(self, name, salary, team_size)

    def show_info(self):
        print(f"Tech Lead: {self.name}, Language: {self.language}, Team Size: {self.team_size}, Salary: Rs.{self.salary}")

emp = Developer('saad',345234,'ror')
emp.show_info()
lead = TechLead("Bilal Ahmad", 220000, "Python", 8)
lead.show_info()
