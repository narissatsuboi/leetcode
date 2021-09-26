"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so "a" is considered a different type of stone
from "A".
"""


class Solution(object):
    # hash set O(n) time | O(n) space
    # for each stone, check whether it matches any of the jewels
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        # also works ...
        # sum(stone in jewels for stone in stones)

        return sum(s in jewel_set for s in stones)

    # brute force O(n2) time | O(n) space
    def numJewelsInStones1(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1
        return count


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"