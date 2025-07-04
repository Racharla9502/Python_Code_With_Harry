# Write a program to input eight numbers from the user and display all the unique numbers (once).

nums = []

for i in range(8):
    num = int(input("Enter a number: "))
    nums.append(num)
print(nums)

unique_nums = set(nums)

print("Unique numbers are:", unique_nums)