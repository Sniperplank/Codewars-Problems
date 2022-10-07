# Probelm Description
"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""

# Output Examples
"""
N/A
"""

# Problem Solution

def get_count(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels:
            count += 1
    return count
