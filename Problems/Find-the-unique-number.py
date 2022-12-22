# Probelm Description
"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
"""

# Output Examples
"""
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
"""

# Problem Solution
def find_uniq(arr):
    not_unique_num = 0
    for i in arr[:3]:
        if arr[:3].count(i) > 1:
            not_unique_num = i
    unique_set = set(arr)
    unique_set.discard(not_unique_num)
    return list(unique_set)[0]
