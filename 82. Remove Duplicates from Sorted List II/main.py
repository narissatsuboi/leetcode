"""
## SITUATION
# Understand the question
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

# Confirm inputs
in: sorted ll w segments containing duplicates
out: sorted ll w/o segments containing duplicates

# Ask clarifying questions

# Brainstorm examples and edge cases
    # head is unique
    head = 1 2 3 3 4 4 5
    head = 1 2         5
    # head is duplicate
    head = 1 1 1 2 3
    head =       2 3
    # duplicate sublist at end
    head = 1 2 2 4 4
    head = 1

## TASK
Naive Approach: Avoiding Pointer Manipulation:
1. create temporary list, append values from ll into list
2. create frequency dictionary with counter
3. list comprehension containing elements that appear only once in the dict
3. feed elements of list into new ll
4. return the next pointer of the dummy list
Downsides: uses extra memory

In Place Approach:
1. Use dummy head node to create a previous pointer
2. Delete duplicate segments by pointing previous pointer to the next
    non-duplicate segment.
"""

from collections import Counter


class ListNode:
    # constructor initializes node object
    def __init__(self, data):
        self.val = data  # assign data
        self.next = None  # next is null


class LinkedList:
    # constructor initialized head node
    def __init__(self):
        self.head = None  # head of empty LL points to null

    # insert new node at beginning of list
    def push(self, new_data):
        new_node = ListNode(new_data)  # initialize new node with new data
        new_node.next = self.head  # point node's next to head
        self.head = new_node  # point head to new node

    # toString
    def to_string(self):
        node = self.head
        list_str = ""
        while node:  # while node doesn't point to null
            list_str += (str(node.val) + "->")
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
        return slow.val

    def deleteDuplicatesNaive(self):
        temp = []  # temp list to feed to counter object

        # traverse through ll, adding elements to list
        current = self.head
        while current:
            temp.append(current.val)
            current = current.next

        # create counter object and list comprehension out of frequencies
        c = Counter(temp)
        temp = [key for key, value in c.items() if value == 1]

        # convert list into new linked list
        dummyll = current = ListNode()

        for i in temp:
            current.next = ListNode(i)
            current = current.next

        return dummyll.next

    def deleteDuplicates(self):
        # create new head
        sentinel = ListNode(0)

        # point previous pointer to sentinel
        prev = sentinel

        # head is now at the second element in the list and is the "current"
        # ptr

        while head:  # traverse to the end of the list
            # if value at head and the next value are the same, we need to
            # advance head until we've left the sublist of duplicates
            # head.next must not be null in order to have values to compare
            if head.next and head.val == head.next.val:  # duplicate segment
                while head.next and head.val == head.next.val:
                    head = head.next
                # now point previous to the next non duplicate element
                prev.next = head.next
            # not in segment of duplicates, shift previous
            else:
                prev = prev.next
            # shift head each iteration
            # this part is like a loop control variable
            head = head.next

        return sentinel.next



