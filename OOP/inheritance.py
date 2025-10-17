#Topic: Inheritance
class Person:
      def __init__(self, firstname='Ali', lastname='Ahmed', age=22, country='Pakistan', city='Lahore'):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.country = country
            self.city = city
            self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
            self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('django')
p1.add_skill('R')
p2 = Person('Umer', 'Umar', 21, 'Pakistan', 'Sialkot')
p2.add_skill('FLask')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    pass

s1 = Student('Manohar', 'Ahmed', 24, 'USA', 'Calfornia')

print(s1.person_info())
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('JavaScript')
print(s1.skills)
