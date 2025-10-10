#Topic: Integer and Float

# interger is number without decimal point 
age = 23
years_of_experience = 3
students_in_class = 16

print("Age:", age)
print("Experience:", years_of_experience, "years")
print("Students:", students_in_class)

# Float means numbers that have decimal points.
gpa = 3.27
print("CGPA:", gpa)


# Basic Arithmetic Operations
# +, -, *, / 

monthly_salary = 85000
months = 12
annual_salary = monthly_salary * months
print("Annual Salary ", annual_salary)

bonus = 15000
total_income = annual_salary + bonus
print("Total Annual Income ", total_income)

expenses = 700000
savings = total_income - expenses
print("Total Savings:", savings)


total_students = 47
buses = 10
students_per_bus = total_students // buses # floor dvision
remaining_students = total_students % buses # mod

print("Students per bus:", students_per_bus)
print("Remaining students:", remaining_students)


# Power and Square Root
# ** is used for power

marks = 5
power = marks ** 3 
square_root = marks ** 0.5

print("Power:", power)
print("Square Root:", square_root)
print("Type of age:", type(age))# type check the datatype of the variable

#Salary Increment Calculation
current_salary = 85000
increment_percentage = 1.5

new_salary = current_salary + (current_salary * increment_percentage / 100)
print(f"After a {increment_percentage}% raise, new salary is: {new_salary}")
