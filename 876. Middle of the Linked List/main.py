"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the
linked list.

If there are two middle nodes, return the second middle node.

Examples:
    head = 1
    head = [1, 2, 3, 4, 5] -> 3rd node, index 3
    head = [1, 2, 3, 4, 5, 6] -> 4th node, index 4

Simple Sol'n:
Traverse the linked list with a accumulator variable and divide by 2,
n is even, the node is at position n/2 + 1

Slow and Fast Pointer Sol'n:
Best for cyclic LL and arrays needing to be traversed at different speeds.

slow = fast = self.head
while fast and fast's next pointer aren't None.
    slow points to its next
    fast points to its next's next (skips two)
cycle stops when fast's next pointer is none, the slow pointer will be back
at the middle element
ODD
head = [1, 2, 3, 4, 5]
       s/f fn
head = [1, 2, 3, 4, 5]
           s     f  fn
head = [1, 2, 3, 4, 5]
              s     f  fn NONE

EVEN
head = [1, 2, 3, 4, 5, 6]
       s/f fn
head = [1, 2, 3, 4, 5, 6]
           s  f  fn
head = [1, 2, 3, 4, 5, 6]
              s     f  fn
head = [1, 2, 3, 4, 5, 6]
                 s     f  fn NONE
"""

import unittest
from collections import deque  # for linkedlist


class Node:
    # constructor initializes node object
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # next is null


class LinkedList:
    # constructor initialized head node
    def __init__(self):
        self.head = None  # head of empty LL points to null

    # insert new node at beginning of list
    def push(self, new_data):
        new_node = Node(new_data)  # initialize new node with new data
        new_node.next = self.head  # point node's next to head
        self.head = new_node       # point head to new node

    # toString
    def linkedlist_to_string(self):
        node = self.head
        list_str = ""
        while node:  # while node doesn't point to null
            list_str += (str(node.data) + "->")
            node = node.next  # point to next node
        list_str += "NULL"

    def find_middle_node(self):
        # initialize slow and fast pointers
        slow = self.head
        fast = self.head

        # transversal until fast's next is null
        while fast and fast.next:
            slow = slow.next  # increment slow once
            fast = fast.next.next  # increment fast twice
        return slow.data


if __name__ == "__main__":
    print("876. Middle of the Linked List")

