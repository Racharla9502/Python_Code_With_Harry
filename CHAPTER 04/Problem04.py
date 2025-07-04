# Write a program to sum a list with 4 numbers.

# Initialize an empty list to store the numbers
numbers = []   

for i in range(4):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
# Calculate the sum of the numbers
print(f"The list of numbers is: {numbers}")
total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")