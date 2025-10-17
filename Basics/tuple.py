#Topic: Tuples

# Tuples are like lists but cannot be changed (immutable).
# Written inside () / list in []

fruits = ("Mango", "Banana", "Apple", "Peach")
print("Fruits Tuple:", fruits)

# Access elements using index
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Tuples can store mixed data types
mixed = ("Orange", 250, True)
print("Mixed Tuple:", mixed)

# Length of tuple
print("Total Fruits:", len(fruits))

# Loop through a tuple
for fruit in fruits:
    print("-", fruit)

# Check if an item exists
print("Mango present", "Mango" in fruits)

# You cannot modify tuples directly, but you can convert to list
temp = list(fruits)
temp.append("Guava")
fruits = tuple(temp)
print("After Adding Guava:", fruits)
