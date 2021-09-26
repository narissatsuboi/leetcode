"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and
return the new string.
"""


class Solution(object):

    # good time, okay memory
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u']

        for letter in s:
            if letter in vowels:
                s = s.replace(letter, "")

        return s

    def removeVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = []

        for letter in s:
            if letter not in vowels:
                result.append(letter)

        return ''.join(result)