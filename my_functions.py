#Task 1: Testing a Calculator (Addition & Subtraction)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b 

#Task 2: Testing an Even Number Checker
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Task 3: Testing a String Reversal Function
def reverse_string(s):
     return s[::-1]

#Task 4: Testing a Palindrome Checker
def is_palindrome(s):
    s = s.lower()  
    if s == s[::-1]:
        return True
    else:
        return False
    
#Task 5: Testing a Maximum Finder in a List
def find_max(numbers):
    return max(numbers)

# ask 6: Testing a Factorial Function 
def factorial(n):
    if n < 0:
        raise ValueError("F is not defined")
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value
    
#Task 7: Testing a Number Sorting Function
def sort_numbers(numbers):
    return sorted(numbers)

#Task 8: Testing a Password Validation Function
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit











