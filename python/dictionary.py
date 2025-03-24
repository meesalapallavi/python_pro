# Step 1: Creating a Dictionary with at least 5 key-value pairs (Student ID: Name)
students = {
    "S001": "Alice",
    "S002": "Bob",
    "S003": "Charlie",
    "S004": "Diana",
    "S005": "Ethan"
}

# 1.1 Adding values to the dictionary
students["S006"] = "Frank"
students["S007"] = "Grace"
print("After Adding:", students)

# 1.2 Updating values in the dictionary
students["S003"] = "Charlotte"  # Update Charlie to Charlotte
print("After Updating:", students)

# 1.3 Accessing a value in the dictionary
print("Accessing S002:", students["S002"])  # Access Bob's name

# 1.4 Creating a nested loop dictionary
# Adding another layer with grades for each student ID
nested_students = {
    "S001": {"Name": "Alice", "Grades": {"Math": 85, "Science": 90}},
    "S002": {"Name": "Bob", "Grades": {"Math": 78, "Science": 82}},
    "S003": {"Name": "Charlotte", "Grades": {"Math": 92, "Science": 88}},
    "S004": {"Name": "Diana", "Grades": {"Math": 74, "Science": 79}},
    "S005": {"Name": "Ethan", "Grades": {"Math": 89, "Science": 94}},
}

# 1.5 Accessing values in a nested dictionary
print("Accessing S003's Science grade:", nested_students["S003"]["Grades"]["Science"])

# 1.6 Printing keys present in a dictionary
print("Keys in students dictionary:", students.keys())
print("Keys in nested_students dictionary:", nested_students.keys())

# 1.7 Deleting a value from the dictionary
del students["S007"]  # Delete the student with ID S007 (Grace)
print("After Deleting:", students)
