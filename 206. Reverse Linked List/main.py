"""
Given the head of a singly linked list, reverse the list, and return the
reversed list.

Approach: Iterative
Use 3 pointers to (1) store head's next (2) point head's next backward (3)
shift all the points down the list one node until the end. Return the
previous pointer which represents the new head.

Examples:
    head -> None,  return head
    head.next ->, return head
    1 2 3 None
    None 3 2 1

Time complexity: O(n)
Space complexity: O(1) in place
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        3 pointer approach, use previous to hold prev node to head, while shifting head down the list. Head             knows where its NEXT node is because before moving pointers we store its next pointer in NEXT node.
        Time complexity: O(n) where n is the number of elements in the list
        Space complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            next = curr.next     # store head's next for later
            curr.next = prev     # flip heads next around to point to prev
            prev = curr          # shift previous one node over
            curr = next          # shift head one node over

        return prev   # the new head of the list
