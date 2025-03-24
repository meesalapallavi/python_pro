import re

# 1. Different ways to create a string
string1 = "Hello, World!"          # Double quotes
string2 = 'Hello, World!'           # Single quotes
string3 = """Hello, World!"""       # Triple quotes for multi-line strings
string4 = str(123)                  # Using str() to convert a number
print("Different ways to create strings:", string1, string2, string3, string4)

# 2. Concatenating two strings using `+` operator
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print("Concatenated string:", concatenated)

# 3. Finding the length of the string
length = len(concatenated)
print("Length of concatenated string:", length)

# 4. Extract a substring
substring = concatenated[0:5]  # Extract "Hello"
print("Extracted substring:", substring)

# 5. Searching in strings using `index()`
position = concatenated.index("World")
print("Position of 'World':", position)

# 6. Matching a string against a regular expression with `re.match()`
pattern = r"Hello"
if re.match(pattern, concatenated):
    print("Pattern matches at the beginning of the string.")
else:
    print("Pattern does not match.")

# 7. Comparing strings
str3 = "Hello"
print("Are str1 and str3 equal?", str1 == str3)         # True if str1 and str3 are identical
print("Are str1 and str2 not equal?", str1 != str2)     # True if str1 and str2 are not identical
print("Is str1 less than str2?", str1 < str2)           # Lexicographical comparison

# 8. `startswith()`, `endswith()`, and lexicographical comparison (similar to compareTo)
print("Does str1 start with 'He'?", str1.startswith("He"))    # True
print("Does str2 end with 'ld'?", str2.endswith("ld"))        # True
comparison = (str1 > str2) - (str1 < str2)  # Lexicographical comparison (-1, 0, or 1)
print("Lexicographical comparison result:", comparison)

# 9. Trimming strings with `strip()`
str_with_spaces = "   Hello World!   "
trimmed = str_with_spaces.strip()
print("Trimmed string:", trimmed)

# 10. Replacing characters in strings with `replace()`
replaced_string = concatenated.replace("World", "Python")
print("String after replacement:", replaced_string)

# 11. Splitting strings with `split()`
split_string = concatenated.split(" ")
print("Split string:", split_string)  # Output: ['Hello', 'World']

# 12. Converting integer objects to strings
number = 123
string_from_number = str(number)
print("String from integer:", string_from_number)

# 13. Converting to uppercase and lowercase
print("Uppercase:", concatenated.upper())     # "HELLO WORLD"
print("Lowercase:", concatenated.lower())     # "hello world"
