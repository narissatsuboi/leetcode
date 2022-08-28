"""
You are given a string s and an integer k. You can choose any character
of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""

"""
LISTEN 
    - k, number of replacements
    - no T/S requirements 
    - Guaranteed non empty string of at least size 1 
    - Output should be int representing longest str 

EXAMPLE 
    s = A B A B    k = 2  2 distinct chars 
        A A A A 
        B B B B 
        
    s = A B A A    k = 2  2 distinct chars 
        A A A A    
        
BRUTE FORCE 
- generate every substring 
- 2 nested for loops 
- TC O(n2) SC O(1) 
        
OPTIMIZE / WALKTHRU 
- duplicated work to review continuously invalid substrings 
starting at i, the first loop
- to improve TC, use sliding window to review substrings along n 
elements once 
- store char counts in array[0] * 26 - 65 OR hashmap 
- substring is valid when len(substring) - char w/ max count <= k
    - when invalid, shift left ptr until valid again 
    - right ptr forward each time (for loop control var) 
"""


def characterReplacement(s, k):
    res = 0

    count = {}

    l = 0

    for r in range(len(s)):
        # char at right ptr
        charR = s[r]

        # update count of char at right pointer
        count[charR] = 1 + count.get(charR, 0)

        # len of curr substring to eval
        subLen = r - l + 1

        # shift left ptr until valid substring
        while subLen - max(count.values()) > k:
            count[s[l]] -= 1    # decrease count of char leaving window
            l += 1              # shrink window
            subLen = r - l + 1  # update len of substring

        # update result to the longer of the previous result or
        # current valid substring
        res = max(res, subLen)

    return res


if __name__ == '__main__':
    s = 'AABABBA'
    k = 1
    print(characterReplacement(s, k))