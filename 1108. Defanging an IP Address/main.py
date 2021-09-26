"""
Given a valid (IPv4) IP address, return a defanged
version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        return '[.]'.join(address.split('.'))

        # result = []
        # fangs = "[.]"
        #
        # curr = 0
        #
        # for i in address:
        #     if i != ".":
        #         result.append(i)
        #     elif i == ".":
        #         result.append(fangs)
        #
        # return ''.join(result)