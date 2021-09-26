"""
Write a function that reverses a string. The input string is given as
an array of characters s.
"""

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    n = len(s) - 1
    midpoint = len(s)//2
    for i in range(0, midpoint):
        s[n], s[i] = s[i], s[n]
        n -= 1


def reverseStringR(s):
    def reverseStringHelper(left, right):
        #  left pointer still has elements to swap
        if left < right:
            s[left], s[right] = s[right], s[left]
            #  continue calling itself
            reverseStringHelper(left + 1, right - 1)
        else:
            return

    # first call to helper
    reverseStringHelper(0, len(s) - 1)


if __name__ == '__main__':
    print("test")
    s = ["h", "e", "l", "l", "o"]
    print(s)
    reverseString(s)
    print(s)

    s = ["h", "e", "l", "l", "o"]
    print(s)
    reverseStringR(s)
    print(s)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
