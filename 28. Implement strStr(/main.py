"""
28. Implement strStr()
Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great
question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().

"""

"""
#1 move sliding window along the string and compare the substring in the 
window with the needle
Time: O(n2), O(length of needle * length of substring) 
Space: O(1) 

#2 Robin-Karp algorithm, rolling hashing with two pointers 
Time: O(n)
Space: O(1) 
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Robin Karp algorithm, compare only substrings with matching 1st ch

        L = len(needle)  # length of needle string
        n = len(haystack)  # length of haystack string

        # check constraints
        if L >=


        # edge case: return 0 if needle length is 0
        if L == 0:
            return 0

        # edge case: needle and haystack are same
        if needle == haystack:
            return 0

        pn = 0  # ptr along length of haystack

        # iterate along length of pn
        while pn < n - L + 1:
            # find 1st position of the 1st needle char in the haystack
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            # compare matching elements one by one until they no longer match
            curr_len = pL = 0
            # while pL < L and pn < n and haystack[pn] == needle[pL]:
            while pL < L and pn < n and haystack[pn] == needle[pL]:

                pL += 1
                pn += 1
                curr_len += 1

            # if elements no longer match AND the length of the substring
            # equals the length of the needle, n -> return the index
            if curr_len == L:
                return pn - L  # index of 1st match
            # else backtrack to last match and repeat
            pn = pn - curr_len + 1

        return -1  # needle not found


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    haystack = "mississippi"
    needle = "pi"
    my_solution = Solution()
    print(haystack, needle, my_solution.strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    my_solution1 = Solution()
    print(haystack, needle, my_solution1.strStr(haystack, needle))

    haystack = "aaa"
    needle = "aaa"
    my_solution2 = Solution()
    print(haystack, needle, my_solution2.strStr(haystack, needle))

    haystack = "hello"
    needle = "ll"
    my_solution3 = Solution()
    print(haystack, needle, my_solution3.strStr(haystack, needle))

