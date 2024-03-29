# Probelm Description
"""
Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the original are swapped.

The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that the 
height and width of the matrix are both positive.
"""

# Output Examples
"""
For example, the transpose of:

| 1 2 3 |
| 4 5 6 |

is

| 1 4 |
| 2 5 |
| 3 6 |
"""

# Problem Solution
from collections import defaultdict

def transpose(m):
    hashmap = defaultdict(list)
    for i in range(len(m[0])):
        for x in (m):
            hashmap[i].append(x[i])
    return list(hashmap.values())
