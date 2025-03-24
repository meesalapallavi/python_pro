# Print "Bright IT Career" Ten Times Using a for Loop
for i in range(10):
    print("Bright IT Career")
    
# Print Numbers from 1 to 20 Using a while Loop
i = 1
while i <= 20:
    print(i)
    i += 1

# Program for Equal (==) and Not Equal (!=) Operators
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)

# Program to Print Odd and Even Numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
# Program to Print Largest Number Among Three Numbers
a, b, c = 10, 20, 15
largest = max(a, b, c)
print("The largest number is:", largest)
# Print Even Numbers Between 10 and 20 Using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
 # Print Numbers from 1 to 10 Using a do-while Loop (Simulated)
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
# Program to Check if a Number is an Armstrong Number
number = 153
original_number = number
result = 0
while original_number != 0:
    digit = original_number % 10
    result += digit ** 3
    original_number //= 10
if result == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong")
# Program to Check if a Number is Prime
number = 29
is_prime = True
if number > 1:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime")
# Program to Check if a Number is a Palindrome
number = 121
original_number = number
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome")
# Program to Check if a Number is Even or Odd Using match (Python 3.10
number = int(input("Enter a number: "))
match number % 2:
    case 0:
        print(f"{number} is even.")
    case 1:
        print(f"{number} is odd.")
# Program to Print Gender Based on Input (M/F) Using match
gender = input("Enter gender (M/F): ").upper()
match gender:
    case 'M':
        print("Gender: Male")
    case 'F':
        print("Gender: Female")
    case _:
        print("Invalid input.")