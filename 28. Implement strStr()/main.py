"""
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int

    Use cases:
    haystack = "hello" needle = "ll" -> 2
    haystack = "aaaaa" needle = "bba" -> -1
    haystack = "" needle = "" -> -1


    """

    lst_haystack = list(haystack)
    lst_needle = list(needle)

    lst = [value for value in lst_haystack if value in lst_needle]
    print(lst)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    strStr(haystack, needle)

    haystack = "aaaaa"
    needle = "bba"

    haystack = ""
    needle = ""

