# Check that a tuple type cannot be changed in python.

my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)

# Attempt to change the first element
my_tuple[0] = 99

print("Modified tuple:", my_tuple)
# This will raise a TypeError because tuples are immutable
# Uncommenting the above line will result in an error
# TypeError: 'tuple' object does not support item assignment
