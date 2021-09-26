"""
1876. Substrings of Size Three with Distinct Characters
A string is good if there are no repeated characters.

Given a string s return the number of good substrings of length three in
s.

Note that if there are multiple occurrences of the same substring,
every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
"""


class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int num of good sstrs in s of size three

        Sliding Window Approach TC: O(N) SC: O(1)
        good = unique chars
        constraints: (1) substring size = 3 (2) good substrings
        clarifying question: empty string return -1?
        example: s = "xyzzaz", "xyz", "yzz", "zza", "zaz" -> "xyz" good substring

        1. establish accumulator variable, result to return
        2. iterate once over the string
        3. track the uniqueness of the charactered (dict)
        4. ask the question - good substring? -> update accumulator
        5. shrink the window, remove the left most window element from consideration
            -> updating character tracker (dict)
        """
        k = 3

        # handle empty string
        if not s:
            return -1  # empty flag

        count = 0  # accumulator

        # create freq dictionary of 1st window, c = 0, 1, 2
        char_freq = {}
        for i in range(len(s) - 2):
            if i not in char_freq:
                char_freq[s[i]] = 0
            char_freq[s[i]] += 1

            # evaluate if constraint is met for a valid window length
            # valid window when c >= k-1
            if i >= k - 1:
                # check if good substring in window
                if len(char_freq) == k:
                    count += 1
                # shrink the left side of the window
                # decrement the char count at the leftmost element
                # remove key value pairs that have 0 as a value

                char_freq[s[i - (k - 1)]] -= 1

                if char_freq[s[i - (k - 1)]] == 0:
                    del char_freq[s[i - (k - 1)]]

        return count


if __name__ == '__main__':
    s = "xyzzaz"
    s2 = "aababcabc"

    print(Solution.countGoodSubstrings(Solution, s))
    print(Solution.countGoodSubstrings(Solution, s2))