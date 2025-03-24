#function for arthmetic operators
def arithmetic_operations(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b if b != 0 else 'undefined (division by zero)'}")

# Example usage
arithmetic_operations(10, 5)

#function for increment and decrement
def increment_decrement(value):
    print(f"Original Value: {value}")
    
    # Increment
    value += 1
    print(f"After Increment: {value}")
    
    # Decrement
    value -= 1
    print(f"After Decrement: {value}")

# Example usage
increment_decrement(5)

#program to check if two numbers are equal
def are_numbers_equal(a, b):
    if a == b:
        print(f"{a} and {b} are equal.")
    else:
        print(f"{a} and {b} are not equal.")

# Example usage
are_numbers_equal(10, 10)
are_numbers_equal(10, 5)

#program for relational operators
def relational_operations(a, b):
    print(f"{a} < {b} : {a < b}")
    print(f"{a} <= {b} : {a <= b}")
    print(f"{a} > {b} : {a > b}")
    print(f"{a} >= {b} : {a >= b}")

# Example usage
relational_operations(10, 5)

#print the smaller and larger number
def find_smaller_larger(a, b):
    smaller = a if a < b else b
    larger = a if a > b else b
    print(f"Smaller number: {smaller}")
    print(f"Larger number: {larger}")

# Example usage
find_smaller_larger(10, 5)