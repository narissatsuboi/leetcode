"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations,
return the final value of X after performing all the operations.
"""

import unittest


class Solution(object):

    # good speed, good memory
    def finalValueAfterOperations1(self, operations):
        plus = operations.count("++X") + operations.count("X++")
        minus = operations.count("--X") + operations.count("X--")
        return plus - minus

    # good speed, bad memory
    def finalValueAfterOperations2(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0  # result

        for operation in operations:
            if "-" in operation:
                x -= 1
            elif "+" in operation:
                x += 1
        return x


if __name__ == "__main__":
    list_of_operations = [["--X", "X++", "X++"], ["++X", "++X", "X++"],
                  ["X++", "++X", "--X", "X--"]]

    my_soln = Solution()

    for operations in list_of_operations:
        print(operations)
        print(my_soln.finalValueAfterOperations1(operations))