"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard
(indexed from 0 to 25). Initially, your finger is at index 0. To type a
character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it
takes to type it with one finger.
"""


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {char: idx for idx, char in enumerate(keyboard)}
        total_time, prior_idx = 0, 0



        return total_time


if __name__ == '__main__':
    my_soln = Solution()
    keyboard = ""abcdefghijklmnopqrstuvwxyz"

