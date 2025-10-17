#Topic: Dictionaries

# A dictionary stores data as key-value pairs inside curly braces {}

fruit_prices = {
    "Mango": 250,
    "Banana": 150,
    "Peach": 300,
    "Guava": 180
}

print("Fruit Prices:", fruit_prices)# Only keys

# Access value by key
print("Price of Mango:", fruit_prices["Mango"])

# Add a new key-value pair
fruit_prices["Watermelon"] = 100
print("After Adding Watermelon:", fruit_prices)

# Update existing value
fruit_prices["Banana"] = 160
print("After Updating Banana:", fruit_prices)

# Remove an item
fruit_prices.pop("Peach")
print("After Removing Peach:", fruit_prices)

# Get all keys and values
print("Fruit Names:", fruit_prices.keys())
print("Fruit Values:", fruit_prices.values())

# Loop through dictionary
for fruit, price in fruit_prices.items():
    print(f"{fruit}: {price} PKR/kg")

# Check if key exists
print("Mango" in fruit_prices)

# Clear all items
fruit_prices.clear()
print("After Clearing:", fruit_prices)
