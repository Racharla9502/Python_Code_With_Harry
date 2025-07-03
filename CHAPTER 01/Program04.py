# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

# Specify the directory you want to list
directory = "."  # "." means current directory

# Get the list of files and directories
contents = os.listdir('/')

# Print the contents
print("Contents of directory:", directory)
for item in contents:
    print(item)
