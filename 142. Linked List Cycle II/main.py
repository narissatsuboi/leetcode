"""
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is
not passed as a parameter.

Do not modify the linked list.

        Story: Given head of LL, return the node that's the start of the
        cycle (1st node to be seen more than once). If no cycle -> null.
        Input: Head, could be null or not.
        Output: Node.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Steps
    # HINT Intersection node isn't necessarily the start node.
    # 1. Find intersection node where slow and fast pointers first meet.
    # 2. Traverse 2 pointers, one from the head and one from the intersection
    # 3. When pointers meet, return entrance node.


class Solution(object):
    def get_intersection_node(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # handle empty list case

        # find the node where slow and fast pointers overlap and return that
        # node
        slow, fast = head, head  # start at head and traverse
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow  # could also return fast

        return None  # no cycle found

    def detectCycle(self, head):
        left = head
        right = self.get_intersection_node(head)

        if right is None:
            return None
        while left != right:
            left = left.next
            right = right.next

        return left


if __name__ == '__main__':
    print("Cyclic LL 2")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
