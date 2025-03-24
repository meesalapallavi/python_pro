class MyClass:
    def __init__(self, x=0, y=0):
        """
        Default constructor with default values for x and y
        :param x: The x coordinate (default is 0)
        :param y: The y coordinate (default is 0)
        """
        print("Constructor called")
        self.x = x
        self.y = y

    def display_values(self):
        print(f"x: {self.x}, y: {self.y}")

# Child class inheriting from MyClass
class MyChildClass(MyClass):
    
    def __init__(self, x=0, y=0):
        """
        Call the parent class constructor and display a message
        """
        super().__init__(x, y)  # Call the constructor of the superclass
        print(f"Child class constructor called with x = {x} and y = {y}")

# 2. Call constructors of superclass from child class
def main():
    # Creating object with default constructor
    print("Creating object with default constructor:")
    obj1 = MyClass()  # Calls default constructor with x=0, y=0
    obj1.display_values()

    # Creating object with one argument constructor
    print("\nCreating object with one argument constructor (x=10):")
    obj2 = MyClass(10)  # Calls constructor with x=10, y=0
    obj2.display_values()

    # Creating object with two argument constructor
    print("\nCreating object with two argument constructor (x=10, y=20):")
    obj3 = MyClass(10, 20)  # Calls constructor with x=10, y=20
    obj3.display_values()

    # 3. Calling constructors from the child class
    print("\nCreating child class object with default constructor:")
    child_obj1 = MyChildClass()  # Calls parent constructor via `super()`

    print("\nCreating child class object with one argument constructor (x=10):")
    child_obj2 = MyChildClass(10)  # Calls parent constructor with x=10

    print("\nCreating child class object with two argument constructor (x=10, y=20):")
    child_obj3 = MyChildClass(10, 20)  # Calls parent constructor with x=10, y=20


if __name__ == "__main__":
    main()
