"""
Given a string s, find the length of the longest substring
without repeating characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Story: given a string return the longest subarray that has no
        repeating characters.
        BF - O(n2) | O(1) Iterate multiple times generating each possibility.
        OPT - O(n) | O(n) Use a freq map and sliding window method.
        :type s: str, could be empty
        :rtype: int, longest substring w/o repeating characters
        """


        window_start = 0
        char_freq = {}  # holds char freq of curr substring

        # 2 "pointers", 1st is for the start of a valid substring, 2nd is
        # for the end of valid subarray
        # iterate thru len of s, each iteration shifts window end boundary
        for window_end in range(len(s)):
            # store char at window end

            # while



if __name__ == '__main__':
    s = "abcabcbb"