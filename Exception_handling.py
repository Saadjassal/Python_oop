#Topic: Exception Handling in Python

try:
    marks = int(input("Enter marks obtained: "))
    total = int(input("Enter total marks: "))
    #total = 0  

    percentage = (marks / total) * 100
    print(f"Percentage: {percentage:.2f}%")

except ZeroDivisionError:
    print("Total marks cannot be zero. Please enter a valid total.")
except ValueError:
    print("Please enter numeric values only.")

else:
    print("Calculation successful!")

finally:
    print("Process completed.")
