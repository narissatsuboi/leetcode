"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "p w w k e w"
          p c n  is next not same as curr? next ++
            p c n

Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstringBF(s):
    """
    BF solution
    TC O(n3) SC O(n)
    :param self:
    :param s:
    :return:
    """
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in chars:
                return False
            chars.add(c)
        return True

    n = len(s)

    res = 0
    for i in range(n): # O(n)
        for j in range(i, n):  # O(n)
            if check(i, j): # O(n)
                res = max(res, j - i + 1)
    return res


def lengthOfLongestSubstring(s):
    """
    Optimized sliding window with hashmap
    TC O(n) SC O(n)
    :param s:
    :return: max length
    """

    haveSeen = {} # { char : index ... }

    start = 0  # maintains beginning of window
    maxLength = 0

    for end in range(len(s)):
        endChar = s[end]
        # check for distinct chars only
        if endChar in haveSeen:
            # don't move start OR update it to the last already seen ch
            start = max(start, haveSeen[endChar] + 1)
        # store the index of the current end char
        haveSeen[endChar] = end

        # update maxlength
        maxLength = max(maxLength, end-start+1)

    return maxLength

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abcabcbb"
    s = "bbbbbbb"

    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstringBF(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
