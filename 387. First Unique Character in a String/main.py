"""
First Unique Character in a String
Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.
"""

from collections import Counter

def firstUniqChar(self, s):
    """
    Get frequencies of chars from Counter and return first index of single
    frequency character.
    :type s: str
    :rtype: int
    """

    # create Counter object and store in var
    char_counts = Counter(s)

    # find the index for the char that occurs once, first
    for index, char_ in enumerate(s):
        if char_counts[char_] == 1:
            return index

    return -1  # default value for no unique characters


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "loveleetcode"
    print(Counter(s))
    print(enumerate(s))