#Topic: Importing Modules & Exploring Python Standard Library

# Import module
import math

marks = 81.7
print("\nCeil:", math.ceil(marks))    # Rounds up
print("Floor:", math.floor(marks))  # Rounds down
print("Square root ", math.sqrt(81))
print("=============================")

# Import specific function from module
from random import choice, randint

students = ["Ali", "Ayesha", "Bilal", "Fatima", "Hassan"]
winner = choice(students)
roll_number = randint(1001, 1020)# randint generate any number between 1001, 1020 both are inclusive it is different from randrange as it does not include the second value (exclusive)

print("\nRandomly selected winner:", winner)
print("Assigned Roll Number:", roll_number)
print("=============================")

# Using datetime module
from datetime import date, datetime
print("\nToday's Date:", date.today())
current_time = datetime.now().strftime("%H:%M:%S")
print("Current Time:", current_time)
print("=============================")

# Using os module
import os

print("\nCurrent Working Directory:", os.getcwd())
print("Files in Current Directory:", os.listdir())

print("=============================")
# Using sys module
import sys

print("\nPython Version Info:")
print(sys.version)
print("Platform:", sys.platform)
