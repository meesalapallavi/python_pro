# my_package/class_a.py
class ClassA:
    def __init__(self):
        self.message = "Hello from Class A!"

    def greet(self):
        return self.message


# my_package/class_b.py
class ClassB:
    def __init__(self):
        self.message = "Hello from Class B!"

    def greet(self):
        return self.message


# my_package/__init__.py
from .class_a import ClassA
from .class_b import ClassB


# main.py
from my_package import ClassA, ClassB

def main():
    # Create an instance of Class A
    class_a_instance = ClassA()
    print(class_a_instance.greet())  # Call method from Class A

    # Create an instance of Class B
    class_b_instance = ClassB()
    print(class_b_instance.greet())  # Call method from Class B

if __name__ == "__main__":
    main()
