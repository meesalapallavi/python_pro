# 1. Generate ArithmeticException Without Exception Handling (ZeroDivisionError in Python)
def generate_arithmetic_exception():
    a = 10
    b = 0
    print(a / b)  # ZeroDivisionError will occur

# 2. Handle the ArithmeticException Using Try-Except Block
def handle_arithmetic_exception():
    try:
        a = 10
        b = 0
        print(a / b)  # ZeroDivisionError will occur
    except ZeroDivisionError as e:
        print(f"Caught exception: {e}")

# 3. Write a Method Which Throws Exception, Call It in Main Class Without Try Block
def raise_exception():
    raise Exception("This is an exception thrown from the method.")

# 4. Write a Program with Multiple Except Blocks
def multiple_exceptions():
    try:
        a = 10
        b = 0
        print(a / b)  # ZeroDivisionError
        
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
        
        none = None
        print(none.upper())  # AttributeError
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    except AttributeError as e:
        print(f"Caught AttributeError: {e}")

# 5. Throw Exception with Your Own Message
def throw_custom_exception():
    raise Exception("This is a custom exception message.")

# 6. Write a Program to Create Your Own Exception
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def raise_custom_exception():
    raise MyCustomException("This is a custom exception!")

# 7. Write a Program with Finally Block
def test_finally():
    try:
        print("Inside try block")
        a = 10
        b = 0
        print(a / b)  # ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Caught exception: {e}")
    finally:
        print("This block will always execute, even after an exception.")

# 8. Generate Arithmetic Exception (ZeroDivisionError)
def generate_arithmetic_exception2():
    a = 10
    b = 0
    print(a / b)  # ZeroDivisionError

# 9. Generate FileNotFoundException
def generate_file_not_found_exception():
    try:
        with open("nonexistent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

# 10. Generate ClassNotFoundException (ModuleNotFoundError in Python)
def generate_class_not_found_exception():
    try:
        __import__('nonexistent_module')  # Will cause ModuleNotFoundError
    except ModuleNotFoundError as e:
        print(f"Caught ModuleNotFoundError: {e}")

# 11. Generate IOError (In Python, IOError is now OSError in most cases)
def generate_io_exception():
    try:
        with open("/nonexistent_directory/nonexistent_file.txt", "r") as f:
            content = f.read()
    except IOError as e:
        print(f"Caught IOError: {e}")

# 12. Generate NoSuchFieldException (Handled as AttributeError in Python)
def generate_no_such_field_exception():
    class MyClass:
        def __init__(self):
            self.name = "Python"
    
    obj = MyClass()
    try:
        print(obj.non_existent_field)  # AttributeError will occur
    except AttributeError as e:
        print(f"Caught AttributeError (NoSuchFieldException in Java): {e}")

# Main function to call all examples
def main():
    print("1. Generate ArithmeticException Without Exception Handling:")
    try:
        generate_arithmetic_exception()
    except Exception as e:
        print(f"Error: {e}")

    print("\n2. Handle the ArithmeticException Using Try-Except Block:")
    handle_arithmetic_exception()

    print("\n3. Write a Method Which Throws Exception, Call It in Main Class Without Try Block:")
    try:
        raise_exception()
    except Exception as e:
        print(f"Error: {e}")

    print("\n4. Program with Multiple Except Blocks:")
    multiple_exceptions()

    print("\n5. Throw Exception with Your Own Message:")
    try:
        throw_custom_exception()
    except Exception as e:
        print(f"Caught exception: {e}")

    print("\n6. Create and Handle Your Own Custom Exception:")
    try:
        raise_custom_exception()
    except MyCustomException as e:
        print(f"Caught custom exception: {e}")

    print("\n7. Program with Finally Block:")
    test_finally()

    print("\n8. Generate Arithmetic Exception (ZeroDivisionError):")
    try:
        generate_arithmetic_exception2()
    except Exception as e:
        print(f"Error: {e}")

    print("\n9. Generate FileNotFoundException:")
    generate_file_not_found_exception()

    print("\n10. Generate ClassNotFoundException (ModuleNotFoundError):")
    generate_class_not_found_exception()

    print("\n11. Generate IOError:")
    generate_io_exception()

    print("\n12. Generate NoSuchFieldException (AttributeError in Python):")
    generate_no_such_field_exception()

# Run the program
if __name__ == "__main__":
    main()

