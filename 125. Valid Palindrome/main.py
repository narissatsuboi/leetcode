"""
Given a string s, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Other approaches (not used):
Copy string, reverse, and compare (multiple iterations along N)
Recursion, call stack large for longer words (overkill)
Use frequency hash table. Iterate over enumeration of hash table and
compare characters at index i with index last (overkill)
"""


def boundedRatio(a, l, r):

    bounded_arr = [False] * len(a)
    # iterate over the given array a
    for idx in range(0, len(a)):
        # calculate x
        x = a[idx] // (idx + 1)
        if isinstance(x, int):
            if l <= x <= r:
                bounded_arr[idx] = True

    # return boolean array
    return bounded_arr


def isPalindrome(s):
    """
    Two pointer Time O(N) Space O(1)
    Space O(N)
    :type s: str
    :rtype: bool
    """
    # convert string to list
    s_lst = list(s)

    # initialize pointers
    left = 0
    right = len(s_lst) - 1

    # continue comparison while left and right pointers haven't crossed or
    # if characters do not match
    while left < right:
        # keep advancing pointer until valid char is found
        while left < right and not s_lst[left].isalnum():
            left += 1
        while left < right and not s_lst[right].isalnum():
            right -= 1

        # characters at each pointer must match to be palindrome
        # convert to lowercase across the board
        if s_lst[left].lower() != s_lst[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    p = "racecar"
    print(isPalindrome(s))

    a = [8, 5, 6, 16, 5]
    c = [False, False, True, False, True]
    l = 1
    r = 3
    print(c)
    print(boundedRatio(a, l, r))

    print(5/2)
    print(5//2)
