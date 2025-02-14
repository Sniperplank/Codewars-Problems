# Probelm Description
"""
https://www.codewars.com/kata/64416600772f2775f1de03f9
"""

# Output Examples
"""
([[2, 5], [5, 3], [5, 5]]), 2)
([[1, 3], [1, 5], [3, 5], [5, 5], [5,3]]), 5)
"""

# Problem Solution

def count_attacking_rooks(rooks):
    # each rank or file has 1 less attacks than the number of rooks it has
    x_dict = {}
    y_dict = {}
    attacks_on_x = 0
    attacks_on_y = 0
    
    # initialize x_dict
    for i in range(8):
        x_dict[i] = 0
    # initialize y_dict
    for i in range(8):
        y_dict[i] = 0
    
    # count rooks on each file from 1 to 8
    for i in rooks:
        x_dict[i[0]] = x_dict[i[0]] + 1

    for i in x_dict:
        if x_dict[i] > 1:
            attacks_on_x += x_dict[i] - 1
    
    # count rooks on each rank from 1 to 8
    for i in rooks:
        y_dict[i[1]] = y_dict[i[1]] + 1

    for i in y_dict:
        if y_dict[i] > 1:
            attacks_on_y += y_dict[i] - 1
    
    total_attacks = attacks_on_x + attacks_on_y
    
    return total_attacks
