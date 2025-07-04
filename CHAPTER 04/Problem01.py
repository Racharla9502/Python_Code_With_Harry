# Write a program to store seven fruits in a list entered by the user.

# Initialize an empty list to store the fruits
fruits = []

# Loop to get seven fruits from the user
for i in range(7):
    # Prompt the user to enter a fruit
    fruit = input(f"Enter fruit {i + 1}: ")
    # Append the entered fruit to the list
    fruits.append(fruit)

# Print the list of fruits
print("The list of fruits is:", fruits)
