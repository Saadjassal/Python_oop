#Topic: Functions in Python

#Without parameters
def greet():
    print("Welcome to Result Processing System!")


# Function with parameters
def calculate_total(oop, dsa, db):
    return  oop + dsa + db

def calculate_percentage(total, subjects=3): # default value for subject
    return total / subjects

# Function returning multiple values
def get_grade_and_status(percentage):
    if percentage >= 80:
        return "A", "Pass"
    elif percentage >= 60:
        return "B", "Pass"
    elif percentage >= 50:
        return "C", "Pass"
    else:
        return "F", "Fail"


#func call
greet()

oop = 78
dsa = 85
db = 74

total = calculate_total(oop, dsa, db)
percentage = calculate_percentage(total)
grade, status = get_grade_and_status(percentage)
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}, Status: {status}")
