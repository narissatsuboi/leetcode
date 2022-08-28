"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
LISTEN 
- guaranteed at least one char in str
- no t/s requirements
- return t/f per given conditions
- conditions are based on matching sets of symbols 

EXAMPLE
0 1 2 3 4 5
( ) [ ] { }
l r 
match, yes, l + 2, r + 2
0 1 2 3 4 5
( ) [ ] { }
    l r 
match, yes, l + 2, r + 2
0 1 2 3 4 5
( ) [ ] { }
        l r 
match, yes, stop, r == n - 1

0 1 2 3  
{ [ ] } valid 

( ( ( ( ) ) ) ) valid 

( [ ) ] invalid 

BRUTE FORCE
- iterate over s with two ptrs
- check the c at left has a matching c at right using if else 
- only works for NON nested input 
OR 
- sort and iterate over with two ptrs TC O(nlogn)

OPTIMIZE
- Need a solution that handles nested input like { [ ] } 
- Use a stack 

WALKTHRU  
append each char to stack 
set ptr on end of s 
from end of s to s, pop a char off of 
"""

def isValidBF(s):
    n = len(s)
    # invalid when len is odd number
    if n % 2 == 1:
        return False

    l, r = 0, 1

    while r < n :
        lChar, rChar = s[l], s[r]
        isPair1 = lChar == '(' and rChar == ')'
        isPair2 = lChar == '[' and rChar == ']'
        isPair3 = lChar == '{' and rChar == '}'

        # must start with an opening brack of any type
        if isPair1 or isPair2 or isPair3:
            l += 2
            r += 2
        else:
            return False
    return True


from collections import deque
def isValid(s):
    """
    Stack implemented with array
    TC O(n) SC O(n)
    :param s:
    :return:
    """

    openClosed = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    stack = []

    for c in s:
        # c is a closed bracket
        if c in openClosed:
            if stack and stack[-1] == openClosed[c]:
                stack.pop()
            else:
                return False
        else: # c is an open bracket
            stack.append(c)

    return not stack


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "()"
    print(isValid(s))

    s = "()[]{}"
    print(isValid(s))

    s = "(]"

    print(isValid(s))




