#Topic: Lists

# A list is a collection that can hold multiple items.
# Lists are written inside square brackets [] and can store different data types(heterogeneous) at same time not similar to array which only contain homogeneous type.

fruits = ["Mango", "Banana", "Apple", "Orange"]
print("Fruit List:", fruits)

# index starts from 0 (0-> first item)
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Lists are mutable(changeable)
fruits[1] = "Jackfruit"
print("Updated list:", fruits)

# append() add item at the end of the list
fruits.append("Watermelon")
print("After Append:", fruits)

# insert() add item at a specific position
fruits.insert(2, "Grapes")
print("After Insert:", fruits)

# remove() delete item by value
fruits.remove("Apple")
print("After Remove:", fruits)

# pop() delete item by index (default: last item)
popped = fruits.pop()
print("Popped Fruit:", popped)
print("After Pop:", fruits)

# We can get a portion of the list using slicing [start:end]
print("First 3 Fruits:", fruits[:3])
print("Middle Fruits:", fruits[1:4])

# Looping through a list
for fruit in fruits:
    print("-", fruit)

# Checking if an item exists in the list
print("Mango" in fruits)

# Find total number of items in the list
print("Total Fruits:", len(fruits))

# sort() arranges items in asc order (A–Z)
fruits.sort()
print("Sorted Fruits:", fruits)

# reverse() flips the order of the list
fruits.reverse()
print("Reversed Fruits:", fruits)

# Lists can hold different data types
mixed_list = ["Banana", 50, True, 99.5]
print("Mixed List:", mixed_list)

fruit_names = ["Mango", "Banana", "Peach", "Guava"]
fruit_prices = [250, 150, 300, 180]  # price per kg in PKR
average_price = sum(fruit_prices) / len(fruit_prices)
print("Average Price per Kg:", average_price)
