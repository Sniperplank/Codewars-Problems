# Probelm Description
"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.
"""

# Output Examples
"""
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
"""

# Problem Solution

def narcissistic( value ):
    sum = 0
    digits = list(str(value))
    for i in str(value):
        sum += int(i)**len(digits)
    return sum == value
