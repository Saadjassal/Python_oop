import datetime  

class Employee:
    # class variables 
    num_of_emps = 0  
    raise_amt = 1.04  # default raise amount

    def __init__(self, first, last, pay):# runs automatically when object is created
        # instance variables 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # every time a new employee is created, increment by 1
        Employee.num_of_emps += 1

    # normal method works with instance variables
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # here self.raise_amt means it’ll first look in the object,
        # if not found, it’ll use the class variable
        self.pay = int(self.pay * self.raise_amt)

    # class method works on the class itself, not specific objects
    @classmethod
    def set_raise_amt(cls, amount):
        # cls refers to the class (Employee)
        # this will update the class variable for all future objects
        cls.raise_amt = amount

    # alternative constructor creates object using a string
    @classmethod
    def from_string(cls, emp_str):
        # split the string into parts
        first, last, pay = emp_str.split('-')
        # return a new Employee object using those given value
        return cls(first, last, pay)

    # static method do not use class or instance data
    @staticmethod
    def is_workday(day):
        # weekday(): Monday=0,Tuesday = 1,..., Sunday=6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# using the static method (no need to create object)
today_date = datetime.date(2025, 10, 10)
print(Employee.is_workday(today_date))  # True or False depending on day


# creating Employee object
e1 = Employee('saad', 'shahbaz', 50000)
print(e1.fullname()) 

e2 = Employee('Umer', 'Umar', 60000)
print(e2.fullname())

# shows how many Employee objects created till now
print(Employee.num_of_emps)

# accessing class variable through instance
print(e1.raise_amt)
# changing raise amount for all using class method
Employee.set_raise_amt(1.07)
print(e1.raise_amt)  # will now reflect updated raise amount

# new Employee from a string (using classmethod)
emp1_str = 'ali-ahmed-100000'
new_emp_1 = Employee.from_string(emp1_str)
print(new_emp_1.pay)
