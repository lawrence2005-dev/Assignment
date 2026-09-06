# List of five favourite fruits
fruits = ["Apple", "Mango", "Banana", "Orange", "Strawberry"]

# Write the fruits to the file
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# Read the fruits from the file
with open("fruits.txt", "r") as file:
    for fruit in file:
        print(fruit.strip())
