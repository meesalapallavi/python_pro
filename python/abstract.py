from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods
class AbstractClass(ABC):
    def __init__(self):
        self.non_abstract_field = "This is a non-abstract method field"

    @abstractmethod
    def abstract_method(self):
        pass  # Abstract method with no implementation

    def non_abstract_method(self):
        return "This is a non-abstract method"


# 2. Create a subclass for the abstract class
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Abstract method implemented in ConcreteClass"

# 3. Create an instance for the child class in the child class and call abstract methods
    def call_abstract_method(self):
        self_instance = ConcreteClass()  # Instance of the child class
        print(self_instance.abstract_method())  # Calling abstract method


# 4. Create an instance for the child class in the child class and call non-abstract methods
    def call_non_abstract_method(self):
        self_instance = ConcreteClass()  # Instance of the child class
        print(self_instance.non_abstract_method())  # Calling non-abstract method


# Main block to demonstrate functionality
if __name__ == "__main__":
    concrete_obj = ConcreteClass()
    
    # Accessing non-abstract method from AbstractClass
    concrete_obj.use_abstract_class()
    
    # Calling abstract method
    concrete_obj.call_abstract_method()

    # Calling non-abstract method
    concrete_obj.call_non_abstract_method()
