# 1. Function to add integer values of an array
def sum_array(arr):
    return sum(arr)

# 2. Function to calculate the average value of an array of integers
def average_array(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

# 3. Program to find the index of an array element
def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1  # Return -1 if the value is not found

# 4. Function to test if array contains a specific value
def contains_value(arr, value):
    return value in arr

# 5. Function to remove a specific element from an array
def remove_element(arr, value):
    while value in arr:
        arr.remove(value)
    return arr

# 6. Function to copy an array to another array
def copy_array(arr):
    return arr.copy()

# 7. Function to insert an element at a specific position in the array
def insert_element(arr, value, position):
    arr.insert(position, value)
    return arr

# 8. Function to find the minimum and maximum value of an array
def min_max_array(arr):
    if len(arr) == 0:
        return (None, None)
    return (min(arr), max(arr))

# 9. Function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]

# 10. Function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for value in arr:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    return list(duplicates)

# 11. Program to find the common values between two arrays
def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 3, 2]
    print("Sum:", sum_array(array))
    print("Average:", average_array(array))
    print("Index of 3:", find_index(array, 3))
    print("Contains 4?", contains_value(array, 4))
    print("Remove 2:", remove_element(array, 2))
    print("Copy of array:", copy_array(array))
    print("Insert 10 at index 2:", insert_element(array, 10, 2))
    print("Min and Max:", min_max_array(array))
    print("Reversed array:", reverse_array(array))
    print("Duplicates:", find_duplicates(array))
    print("Common values with [2, 3, 6]:", common_values(array, [2, 3, 6]))
# 12. Method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

# 13. Method to find the second largest number in an array
def second_largest(arr):
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None  # Not enough unique elements
    unique_arr.sort()
    return unique_arr[-2]

# 14. Method to find the second largest number in an array (duplicate entry removed)
# This is the same as the previous method.

# 15. Method to find number of even numbers and odd numbers in an array
def count_even_odd(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# 16. Function to get the difference of largest and smallest value
def difference_max_min(arr):
    if len(arr) == 0:
        return None  # No elements to compare
    return max(arr) - min(arr)

# 17. Method to verify if the array contains two specified elements (12, 23)
def contains_two_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# 18. Program to remove duplicate elements and return the new array
def remove_duplicates_and_return(arr):
    return list(set(arr))

# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 2, 3, 12, 23, 12, 2]
    
    print("Remove duplicates:", remove_duplicates(array))
    print("Second largest number:", second_largest(array))
    even_count, odd_count = count_even_odd(array)
    print("Even count:", even_count, "Odd count:", odd_count)
    print("Difference between max and min:", difference_max_min(array))
    print("Contains 12 and 23?", contains_two_elements(array, 12, 23))
    print("Remove duplicates and return new array:", remove_duplicates_and_return(array))
