#print your name
print("pallavi")
# This is a single-line comment

"""
This is a multi-line comment.
It can span across multiple lines.
"""

# Defining variables of different data types
integer_var = 42               # Integer data type
boolean_var = True             # Boolean data type
char_var = 'A'                 # Character data type (in Python, characters are just strings of length 1)
float_var = 3.14               # Float data type
double_var = 3.14159265        # In Python, there's no separate double type; we use float for decimals

# Printing the values of each variable
print("Integer Value:", integer_var)
print("Boolean Value:", boolean_var)
print("Character Value:", char_var)
print("Float Value:", float_var)
print("Double Value (float in Python):", double_var)
# Defining a global variable
var = "I am a global variable"

def my_function():
    # Defining a local variable with the same name as the global variable
    var = "I am a local variable"
    print("Inside the function:", var)  # This will print the local variable

# Calling the function to print the local variable
my_function()

# Printing the global variable
print("Outside the function:", var)  # This will print the global variable