# Probelm Description
"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""

# Output Examples
"""
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

# Problem Solution

def generate_hashtag(s):
    if len(s) > 140:
        return False
    if len(s) == 0:
        return False
    ans = "#"
    words = s.split()
    for i in words:
        firstLetter = i[0].upper()
        restOfWord = i[1:].lower()
        ans += firstLetter + restOfWord
    return ans
