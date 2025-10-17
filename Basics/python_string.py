#Topic: STRINGS


#creating strings
first_name = "Saad"
last_name = "Shahbaz"
city = "Lahore"
occupation = "Data Analyst"

# we can make strings using single, double, and triple quotes based on the need, exp. if the text contains a single quote ('), we can use double quotes (") to avoid errors.
quote = 'Work hard in silence.'
dialogue = "Ali said, 'Python is actually fun!'"
multi_line = """with using triple quotes the string
will appear as it is (the way you declared it in multiple lines)."""

print(first_name, last_name)
print(multi_line)


# String Concatenation ( when using string + have a different meaning, here it is used to join two or more strings)
full_name = first_name + " " + last_name
intro = "My name is " + full_name + " and I live in " + city + "."
print(intro)


#String Length and indexing
print("Length:", len(full_name))
print("First char:", full_name[0]) # index start from 0
print("Last char:", full_name[-1]) 
print("Middle:", full_name[1:4])


#String Methods
name = "   Ahmed   "
print("Before strip:", name)  # shows spaces 
print("After strip:", name.strip())     # removes spaces from start and end

email = "hello@gmail.com"
print("uppercase:", email.upper())
print("domain check:", email.endswith("@gmail.com"))# true/ false
print("Count of 'a' in email:", email.count('a'))


#string accessing and modification
cnic = "11111-1111111-1"
masked = cnic[:6] + "******" + cnic[-2:]
print("Original CNIC:", cnic)
print("Masked CNIC:", masked)


#String Formatting
age = 23
profession = "Software Engineer"
city = "Lahore"

# f-string 
print(f"{full_name} is a {profession} from {city}, aged {age}.")

# using format()
info = "{} works as a {} in {}."
print(info.format("Umer Malik", "UI Designer", "Lahore"))


#Splitting and Joining
skills = "Python,SQL,Power BI,Excel"
skills_list = skills.split(",")
print("Skills List:", skills_list)

joined = " | ".join(skills_list)
print("Joined Skills:", joined)


#Checking Content
student_name = "ahsan"
print("Is alphabetic:", student_name.isalpha())
print("Is lowercase:", student_name.islower())

contact = "0325556677"
print("Is digit:", contact.isdigit())

mixed = "Saad123"
print("Is alphanumeric:", mixed.isalnum())


