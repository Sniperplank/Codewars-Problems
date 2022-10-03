# Probelm Description
"""
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace,
while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.
"""

# Output Examples
"""
N/A
"""

# Problem Solution

def reverse_alternate(string):
    words = string.split() # put the words in an array
    for i, x in enumerate(words): # loop through array of words
        if i % 2 == 1: # if the index of a word is odd
            x = x[::-1] # reverse the word
            words = words[:i]+[x]+words[i+1:] # replace the word in the array
    return " ".join(words) # return the joined array of words
