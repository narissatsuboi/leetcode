
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

    def find_middle_node(self):
        # initialize slow and fast pointers
        slow = self.head
        fast = self.head

        # transversal until fast's next is null
        while fast and fast.next:
            slow = slow.next  # increment slow once
            fast = fast.next.next  # increment fast twice
        return slow.val
