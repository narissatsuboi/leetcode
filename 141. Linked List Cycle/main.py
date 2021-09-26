"""
Given head, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        Story: given a head of all, find a cycle such that a node can be
        reached again by following the next pointer.
        Clarify: Is an empty LL considered cyclic? - No.
        Input: ListNode head pointing to null or next Node
        Output: True if cycle found.
        :type head: ListNode
        :rtype: bool
        """

        # Handle empty LL case
        if head is None:
            return False

        # LL is NOT empty -> traverse the list looking for cycle
        # cycle found when 2 offset pointers overlap and next is not null
        slow, fast = head, head  # pointers start at head
        while fast is not None and fast.next is not None:
            fast = fast.next.next  # set fast ahead two nodes
            slow = slow.next  # move slow ahead one node
            # continue until they overlap
            if slow == fast:
                return True  # cycle found

        return False  # next reached None


if __name__ == '__main__':
    print("Cyclic LL")
