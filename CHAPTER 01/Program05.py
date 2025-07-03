# Label the program written in problem 4 with comments.

# import the os module to interact with the operating system
import os  

# Specify the directory you want to list
directory = "." # "." means current directory

# Get the list of entries (files and directories) in the specified directory
# os.listdir() returns a list of the names of the entries in the directory given by path
contents = os.listdir(directory) 

# Print the contents of the directory
print("Contents of directory:", directory)

# This loop goes through each item in the contents list and prints it
for item in contents:
    print(item)
