"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing
n unique integers such that they add up to 0.
"""
from typing import List
import unittest


class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        Approach: Use symmetrical values on n divided by 2.
        When n is odd, add 0 as a filler element.
        :param n: size of output array
        :return: array of elements that sum to 0
        """

        result = []  # holds numbers which sum to 0

        # address case of odd n
        if n % 2 == 1:
            result.append(0)
            n -= 1

        # address case of even n
        while n > 0:
            result.append(n//2)
            result.append(-n//2)
            n -= 2

        return result


if __name__ == '__main__':
    my_solution = Solution()

    # even examples
    print("Even Examples")
    print(my_solution.sumZero(0))
    print(my_solution.sumZero(2))
    print(my_solution.sumZero(4))
    print(my_solution.sumZero(6))

    print("\nOdd Examples")
    # odd examples
    print(my_solution.sumZero(1))
    print(my_solution.sumZero(3))
    print(my_solution.sumZero(5))
    print(my_solution.sumZero(7))

