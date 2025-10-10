# Topic: Sets

# A set is a collection of unique items, written inside curly braces {}

fruits = {"Mango", "Banana", "Apple", "Guava", "Mango"}
print("Fruits Set:", fruits)  # Duplicates are removed automatically

# Add a new item
fruits.add("Peach")
print("After Adding Peach:", fruits)

# Remove an item
fruits.remove("Banana")
print("After Removing Banana:", fruits)

# Check if an item exists
print("Mango" in fruits)

# Loop through a set
for fruit in fruits:
    print("-", fruit)

# Set operations
seasonal = {"Mango", "Watermelon", "Peach"}
common = fruits.intersection(seasonal)
print("Common Fruits:", common)

all_fruits = fruits.union(seasonal)
print("All Fruits:", all_fruits)
