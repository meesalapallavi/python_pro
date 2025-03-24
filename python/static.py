class MyClass:
    # 1. Define a static variable
    static_variable = "I am static"

# 1. Access the static variable through the class
print("Access through class:", MyClass.static_variable)

# 2. Access the static variable through an instance
instance1 = MyClass()
print("Access through instance:", instance1.static_variable)

# 3. Change the static variable within an instance
instance1.static_variable = "Changed within instance"
print("After change in instance:")
print("Instance1:", instance1.static_variable)      # Changes only for instance1
print("Class access:", MyClass.static_variable)     # Remains unchanged for the class

# 4. Change the static variable within the class
MyClass.static_variable = "Changed within class"
print("After change in class:")
print("Class access:", MyClass.static_variable)     # Updates for all instances
print("Instance1 access:", instance1.static_variable) # Remains as it was set directly
