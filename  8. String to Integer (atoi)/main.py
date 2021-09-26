"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

#1 Read in and ignore any leading whitespace.

#2 Check if the next character (if not already at the end of the string)
is '-' or '+'. Read this character in if it is either. This determines if
the final result is negative or positive respectively. Assume the result is
positive if neither is present.

#3 Read in next the characters until the next non-digit charcter or the end of
the input is reached. The rest of the string is ignored.

#4 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
If no digits were read, then the integer is 0. Change the sign as necessary
(from step 2).

#5 If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then clamp the integer so that it remains in the range. Specifically,
integers less than -231 should be clamped to -231, and integers greater than
231 - 1 should be clamped to 231 - 1.

#6 Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest
of the string after the digits.
"""


def myAtoi(s):
    """
    :type s: str
    :rtype: int

    Use cases:
    '42' -> 42
    '   -42' -> -42
    '9999999999999' -> MAX_INT
    '1312adfasdf' -> 1312

    'abc123' -> 0
    '+abc123' -> 0

    Design considerations:
    1. WS in front
    2. -/+ symbol, or no symbol means +
    3. numbers
    4. int constrained between MIN_INT and MAX_INT
    5. non-numeric characters after numbers

    Time O(N) N is num characters
    Space O(1)
    """

    MAX_INT = 2 ** 31 - 1  # 2147483647
    MIN_INT = - 2 ** 31  # - 2147483648

    i = 0  # idx to iterate through the str
    res = 0  # store final result
    negative = 1

    # whitespace
    while i < len(s) and s[i] == ' ':
        i += 1  # keep iterating until non WS character is found

    # +/-
    if i < len(s) and s[i] == '-':
        i += 1  # advance iterator
        negative = -1
    elif i < len(s) and s[i] == '+':
        i += 1

    # check numbers 0-9
    digits = set('0123456789')  # O(1)
    while i < len(s) and s[i] in digits:
        # current result cannot be more than max_int / 10 bc after
        # multiplying  by ten in the next line it could overflow

        if res > MAX_INT / 10 or (res == MAX_INT / 10 and int(s[i]) > 7):
            return MAX_INT if negative == 1 else MIN_INT

        # update res if passed constraint check
        res = res * 10 + int(s[i])
        i += 1

    # check constraint
    return res * negative  # apply sign


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "   -42"
    print(2**31-1)