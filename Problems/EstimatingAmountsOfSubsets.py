# Probelm Description
"""
Given a set of elements (integers or string characters, characters only in RISC-V) that may occur more than once, we need to know the amount of subsets that none of their values have repetitions.

Let's see with an example:

set numbers = {1, 2, 3, 4}
The subsets are:

{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4},{3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}} (15 subsets, as you can see the empty set, {}, is not counted)
Let's see an example with repetitions of an element:

set letters= {a, b, c, d, d}
The subsets for this case will be:

{{a}, {b}, {c}, {d}, {a,b}, {a,c}, {a,d}, {b,c}, {b,d},{c,d}, {a,b,c}, {a,b,d}, {a,c,d}, {b,c,d}, {a,b,c,d}} (15 subsets, only the ones that have no repeated elements inside)
The function est_subsets() (javascript: estSubsets()) will calculate the number of these subsets.

It will receive the array as an argument and according to its features will output the amount of different subsets without repetitions of its elements.
"""

# Output Examples
"""
est_subsets([1, 2, 3, 4]) == 15
est_subsets(['a', 'b', 'c', 'd', 'd']) == 15
"""

# Problem Solution

def est_subsets(arr):
    # remove any repeated values
    arr = sorted(set(arr))            
    # the number of subets is 2 to the power of n where n is the number of elements in a list
    subsets_num = 2 ** len(arr) - 1 # we take one from the result because we dont want the empty subset
    return subsets_num 
