# 1. Class with Private Fields and Methods
class PrivateClass:
    def __init__(self):
        self.__private_field = "This is a private field"
    
    def __private_method(self):
        return "This is a private method"
    
    def main_method(self):
        print(self.__private_field)          # Accessing private field
        print(self.__private_method())       # Calling private method


class SubClass(PrivateClass):
    def access_private(self):
        # Attempting to access private fields and methods from the superclass
        try:
            print(self.__private_field)      # This will raise an AttributeError
        except AttributeError as e:
            print("Error accessing private field:", e)
        
        try:
            print(self.__private_method())   # This will raise an AttributeError
        except AttributeError as e:
            print("Error accessing private method:", e)


# 2. Class with Protected Fields and Methods
class ProtectedClass:
    def __init__(self):
        self._protected_field = "This is a protected field"
    
    def _protected_method(self):
        return "This is a protected method"


# Accessing protected fields and methods in the same package
class SamePackageClass:
    def __init__(self):
        protected_obj = ProtectedClass()
        print(protected_obj._protected_field)   # Accessing protected field
        print(protected_obj._protected_method()) # Accessing protected method


# Accessing protected fields and methods from a subclass in a different package
class DifferentPackageSubclass(ProtectedClass):
    def access_protected(self):
        print(self._protected_field)      # Accessing protected field
        print(self._protected_method())    # Accessing protected method


# 3. Class with Public Fields and Methods
class PublicClass:
    def __init__(self):
        self.public_field = "This is a public field"
    
    def public_method(self):
        return "This is a public method"


# Accessing public fields and methods in the same package
class AnotherClass:
    def __init__(self):
        public_obj = PublicClass()
        print(public_obj.public_field)          # Accessing public field
        print(public_obj.public_method())       # Accessing public method


# Main block to demonstrate functionality
if __name__ == "__main__":
    # Testing PrivateClass
    obj = PrivateClass()
    obj.main_method()  # Print private fields and call private method
    
    sub_obj = SubClass()
    sub_obj.access_private()  # Attempt to access private members
    
    # Testing ProtectedClass
    same_package_obj = SamePackageClass()

    # Note: To demonstrate access from a subclass in a different package,
    # you would need to have a separate module structure in a real environment.
    different_package_obj = DifferentPackageSubclass()
    different_package_obj.access_protected()
    
    # Testing PublicClass
    another_obj = AnotherClass()
