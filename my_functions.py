""""""

#Task 1: Testing a Calculator (Addition & Subtraction)
def add(a, b):
    """Return the sum of a and b"""
    return a + b

def subtract(a, b):
    """Return the subtraction of a and b"""
    return a - b 

#Task 2: Testing an Even Number Checker
def is_even(n):
    """Returning True if n is even, False otherwise"""
    if n % 2 == 0:
        return True
    else:
        return False

#Task 3: Testing a String Reversal Function
def reverse_string(s):
     """Return reverse of input string s"""
     return s[::-1]

#Task 4: Testing a Palindrome Checker
def is_palindrome(s):
    """Return True if s is palindrome, False otherwise"""
    s = s.lower()  
    if s == s[::-1]:
        return True
    else:
        return False
    
#Task 5: Testing a Maximum Finder in a List
def find_max(numbers):
    """Return the maximum number"""
    return max(numbers)

# ask 6: Testing a Factorial Function 
def factorial(n):
    """Return factorial of non negative intiger n"""
    if n < 0:
        raise ValueError("F is not defined")
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value
    
#Task 7: Testing a Number Sorting Function
def sort_numbers(numbers):
    """Return a sorted list of numbers"""
    return sorted(numbers)

#Task 8: Testing a Password Validation Function
def is_valid_password(password):
    """Return false if the password is not valid"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit











