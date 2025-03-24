# Read text from a file and print to the console

file_name = 'C:\Users\rames\OneDrive\Desktop\python assignment\python\input.txt' 
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")
