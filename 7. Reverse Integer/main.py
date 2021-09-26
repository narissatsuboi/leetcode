"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).
"""


def reverse(x):
    """
    Time O(N)
    Space O(1)
    :type x: int
    :rtype: int
    """

    # Initialize reverse_x = 0
    # Iterate through digits in x
    # Pop the last digit from x, store
    # Divide x by 10
    # Check for overflow
    # Return reverse_x

    def mod(number, m):
        """
        Returns the correct modulus of a number and a divider, even if number is
        negative.
        :type number: int
        :type m: int
        :rtype: int
        """
        if number < 0:
            return number % -m  # adjusted mod for negative number
        return number % m

    def divide(divisor, dividend):
        """
        Correct floor division with negative numbers.
        eg. -123/12 = -12 instead of -13 (-12.3 floored)
        :type divisor:
        :type dividend:
        :rtype: int
        """

        return int(divisor * 1.0 / dividend)

    # To check for final value within 32-bit integer range
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    reverse_x = 0  # holds reversed integer

    while x:
        # Copy last digit of x with modulus 10
        last_digit = mod(x, 10)

        # Make x one digit smaller
        x = divide(x,10)

        # Check for 32 bit overflow before calculating final result
        if (reverse_x > divide(MAX_INT, 10)) or (reverse_x == divide(
                MAX_INT, 10) and last_digit > 7):
            return 0
        if (reverse_x < divide(MIN_INT, 10)) or (reverse_x == divide(
                MIN_INT, 10) and last_digit < -8):
            return 0

        # Update reversed int value by increasing digits place by 1 and
        # adding the stored last digit
        reverse_x = reverse_x * 10 + last_digit

    return reverse_x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [12, 34, 510]
    print(arr)
    for i in range(len(arr)):
        print(reverse(arr[i]), end=' ')

