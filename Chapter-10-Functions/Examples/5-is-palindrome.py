"""
A palindrome is a word or phrase which reads the same in both directions.
example - deed, level, malayalam, rats live on no evil star
Ignore spaces while checking for palindrome
"""

def ispalindrome(s):
    t = s.lower()
    left = 0
    right = len(t) - 1

    while right >= left:
        if t[left] == '':
            left += 1
        if t[right] == '':
            right -= 1
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True

print(ispalindrome('malayalam'))
print(ispalindrome('Rats live on no evil star'))

# Since string are immutable the sting converted to lowercase has to be collected in another string t