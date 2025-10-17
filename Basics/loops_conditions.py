#Topic: Conditions and Loops in Python

# IF, ELIF, ELSE statements

student_name = "Saad"
score = 90

if score >= 90:
    print(f"{student_name} got an A grade.")
elif score >= 80:
    print(f"{student_name} got a B grade.")
elif score >= 70:
    print(f"{student_name} got a C grade.")
else:
    print(f"{student_name} needs improvement.")


# NESTED IF
attendance = 92
if score >= 80:
    if attendance >= 90:
        print(f"{student_name}  eligible.")
    else:
        print(f"{student_name}  attendance low.")


# FOR LOOP
students = ["Ali", "Haseeb", "Azeem", "Umer"]
print("\nStudent Names:")
for s in students:
    print("-", s)


# Using range() with for loop
print("\nRoll Numbers:")
for i in range(1, 6):# sstarts for 1 if not mentioned like in this case then 0, last number is not included.
    print("Roll No:", i)


# WHILE LOOP
count = 1
print("While Loop")
while count <= 3:
    print(f"Checking exam paper {count}")
    count += 1


# LOOP WITH BREAK and CONTINUE
print("Break and Continue")
for s in students:
    if s == "Umer":
        print("Skipping Bilal (absent)...")
        continue
    if s == "Azeem":
        print("stopping check!")
        break
    print("Processing:", s)
