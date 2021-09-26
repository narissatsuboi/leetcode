"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
"""


from collections import Counter

def isAnagramSort(s, t):
    """
    Sort characters of each string array, check equality of arrays.
    Time O(NlogN), standard sorting fxn TC
    Space O(1), uses extra space but stays constant.

    :type s: str
    :type t: str
    :rtype: bool
    """

    # check sizes to avoid unneeded operations
    if len(s) != len(t):
        return False

    # covert string to sorted list
    s_lst = sorted(list(s))
    t_list = sorted(list(t))

    print(s_lst)
    print(t_list)

    return s_lst == t_list


def isAnagramHash(s, t):
    """
    Create two dictionaries and compare character frequencies.
    If equal, true.
    Time O(N)
    Space O(1), uses extra space but stays constant.

    :type s: str
    :type t: str
    :rtype: bool
    """

    # check sizes to avoid unneeded operations
    if len(s) != len(t):
        return False

    # build Counter hash tables, char : freq
    counter_s = Counter(s)
    counter_t = Counter(t)

    # check for anagram condition
    are_anagrams = counter_s == counter_t

    if are_anagrams:
        return True

    return False


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    print(isAnagramSort(s, t))



