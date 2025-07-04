# Write a program to accept marks of 6 students and display them in a sorted manner.

# Initialize an empty list to store the marks
marks = []  

# Loop to get marks from the user
for i in range(6):
    mark = float(input(f"Enter the marks of student {i + 1}: "))
    marks.append(mark)

print(f"The marks entered are: {marks}")

marks.sort()

print(f"The sorted marks are: {marks}")