"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.

Return the shuffled string.
"""


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        # initialize array of length s
        shuffled_arr = [''] * len(s)
        # iterate over indices
        for idx in indices:
            # for each index, store the corresponding character to the array
            # at that index
            shuffled_arr[indices[idx]] = s[idx]

        # join the array and return the string
        return ''.join(shuffled_arr)

