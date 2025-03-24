class MyClass:
    
    # Method with one parameter
    def print_values(self, a):
        print(f"Value of a: {a}")

    # Method with two parameters
    def print_values(self, a, b):
        print(f"Value of a: {a}, Value of b: {b}")

# Create an object of MyClass
obj = MyClass()

# Call methods
obj.print_values(10,30)    # Will call the method with one parameter
obj.print_values(10, 20) # Will call the method with two parameters
class MyClass:
    
    # Method with one integer parameter
    def print_values(self, a):
        if isinstance(a, int):
            print(f"Integer value: {a}")
    
    # Method with one string parameter
    def print_values(self, a):
        if isinstance(a, str):
            print(f"String value: {a}")

# Create an object of MyClass
obj = MyClass()

# Call methods
obj.print_values(10)    # Will print the integer method
obj.print_values("Hello")  # Will print the string method
class MyClass:
    
    # Method that can handle both int and str by type checking
    def print_values(self, a):
        if isinstance(a, int):
            print(f"Integer value: {a}")
        elif isinstance(a, str):
            print(f"String value: {a}")
        else:
            print(f"Unsupported type: {type(a)}")

# Create an object of MyClass
obj = MyClass()

# Call method with different types
obj.print_values(10)        # Integer
obj.print_values("Hello")   # String
obj.print_values([1, 2, 3]) # Unsupported type
class MyClass:
    
    # Method with one or more integer parameters
    def print_values(self, *args):
        if all(isinstance(i, int) for i in args):  # Check if all arguments are integers
            print(f"Values: {', '.join(map(str, args))}")
        else:
            print("All arguments must be integers.")

# Create an object of MyClass
obj = MyClass()

# Call method with different number of parameters
obj.print_values(10)             # One parameter
obj.print_values(10, 20)         # Two parameters
obj.print_values(10, 20, 30)     # Three parameters
obj.print_values(10, "Hello")    # Invalid call

