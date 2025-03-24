class A:
    def method1(self):
        return "Method 1 from Class A"

    def method2(self):
        return "Method 2 from Class A"

    def overridden_method(self):
        return "Overridden method in Class A"


class B(A):
    def method1(self):
        return "Method 1 from Class B"

    def method2(self):
        return "Method 2 from Class B"

    def overridden_method(self):
        return "Overridden method in Class B"


class C(B):
    def method1(self):
        return "Method 1 from Class C"

    def method2(self):
        return "Method 2 from Class C"

    def overridden_method(self):
        return "Overridden method in Class C"


# Main class to create objects and call methods
class Main:
    def __init__(self):
        # Creating objects for each class
        a = A()
        b = B()
        c = C()

        # Calling methods for class A
        print("Class A Methods:")
        print(a.method1())
        print(a.method2())
        print(a.overridden_method())

        # Calling methods for class B
        print("\nClass B Methods:")
        print(b.method1())
        print(b.method2())
        print(b.overridden_method())

        # Calling methods for class C
        print("\nClass C Methods:")
        print(c.method1())
        print(c.method2())
        print(c.overridden_method())

        # Calling overridden methods using superclass reference
        print("\nCalling overridden methods with superclass reference:")
        a_ref_b = b  # Reference of B as A
        a_ref_c = c  # Reference of C as A
        print(a_ref_b.overridden_method())  # Calls B's overridden method
        print(a_ref_c.overridden_method())  # Calls C's overridden method


# Instance creation to execute the main method
if __name__ == "__main__":
    Main()

# --------------------
# Now demonstrating runtime polymorphism with data members/instance variables

class AWithData:
    def __init__(self):
        self.data = "Data in Class A"

    def overridden_data(self):
        return "Overridden data in Class A"


class BWithData(AWithData):
    def __init__(self):
        super().__init__()  # Call A's constructor
        self.data = "Data in Class B"

    def overridden_data(self):
        return "Overridden data in Class B"


class CWithData(BWithData):
    def __init__(self):
        super().__init__()  # Call B's constructor
        self.data = "Data in Class C"

    def overridden_data(self):
        return "Overridden data in Class C"


# Main class to create objects and call data member methods
class MainWithData:
    def __init__(self):
        # Creating objects for each class with data members
        a = AWithData()
        b = BWithData()
        c = CWithData()

        # Accessing and printing data members
        print("Class A Data:", a.data)
        print("Class B Data:", b.data)
        print("Class C Data:", c.data)

        # Calling overridden data methods
        print("\nCalling overridden data methods with superclass reference:")
        a_ref_b = b  # Reference of B as A
        a_ref_c = c  # Reference of C as A
        print(a_ref_b.overridden_data())  # Calls B's overridden data method
        print(a_ref_c.overridden_data())  # Calls C's overridden data method


# Instance creation to execute the main method for data members
if __name__ == "__main__":
    MainWithData()
