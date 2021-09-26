"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list,
delete all duplicates such that each element
appears only once. Return the linked list sorted as well.

Inputs: sorted ll w duplicates
Outputs: sorted ll w/o duplicates

ll = 1 -> 1 -> 2
ll = 1 -> 2

ll = 1 -> 1 -> 2 -> 3 -> 3
ll = 1 -> 2 -> 3

Naive Sol'n:
Tranverse the ll, turn into a python list, then a set which unique elements,
and then go back and push them back into the ll in backwards order.

Test
ll = 1 -> 1 -> 2 -> 3 -> 3 NULL
     c   cn   cnn
ll = 1 -> 1 -> 2 -> 3 -> 3 NULL
     c         cn   cnn
    node at s next point to f
ll = 1 -> 2 -> 3 -> 3 NULL
          c   cn   cnn
    node at s next point to f
ll = 1 -> 2 -> 3 -> 3 NULL
               c   cn   cnn
ll = 1 -> 2 -> 3 -> NULL
               c   cn   cnn
    node at s next point to f
"""


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
        self.head = new_node       # point head to new node

    # toString
    def to_string(self):
        node = self.head
        list_str = ""
        while node:  # while node doesn't point to null
            list_str += (str(node.val) + "->")
            node = node.next  # point to next node
        list_str += "NULL"

    def delete_duplicates(self):
        current = self.head
        while current and current.next:
            # compare vals at current and current's next
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return self.head

"""
Test
ll = 1 -> 1 -> 2 -> 3 -> 3 NULL
    s/f   
ll = 1 -> 1 -> 2 -> 3 -> 3 NULL
     s         f    
    node at s next point to f
ll = 1 -> 2 -> 3 -> 3 NULL
          s    f 
    node at s next point to f
"""









