# Probelm Description
"""
You are given two strings (st1, st2) as inputs. Your task is to return a string containing the numbers in st2 which are not in str1. 
Make sure the numbers are returned in ascending order. All inputs will be a string of numbers.
"""

# Output Examples
"""
findAdded('4455446', '447555446666'); // '56667'
findAdded('44554466', '447554466'); // '7'
findAdded('9876521', '9876543211'); // '134'
findAdded('678', '876'); // ''
findAdded('678', '6'); // ''
"""

# Problem Solution

def findAdded(s1, s2):
    output = ''
    count = {}
    for i in s2:
        count[i] = 1 + count.get(i, 0)
    for i in s1:
        count[i] = count.get(i, 0) - 1
    for k in count:
        output += k * count[k]
    return "".join(sorted(output))

print(findAdded('4455446', '447555446666'))



