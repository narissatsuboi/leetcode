class ListNode:
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # next is null


class LinkedList:
    def __init__(self, list_of_data = None):
        self.head = None  # head of empty LL points to null
        if list_of_data is not None:
            n = len(list_of_data) - 1
            while n >= 0:
                self.prepend(list_of_data[n])
                n -= 1

    def prepend(self, new_data):
        """
        Creates new node (given data) and inserts at front of list.
        O(n) time, O(1) space.
        :param new_data: Node to precede new node.
        """
        new_node = ListNode(new_data)  # initialize new node with new data
        new_node.next = self.head  # point node's next to head
        self.head = new_node  # point head to new node

    def insert_after(self, prev_node, new_data):
        """
        Inserts a given node after a given node.
        O(n) time, O(1) space.
        :param prev_node: Node to precede new node.
        :param new_data: New node.
        :return: False if prev node isn't in linked list
        """
        # check if previous node exists
        if prev_node is None:
            return False
        # create new node
        new_node = ListNode(new_data)
        # point new node's next to prev_node's next
        new_node.next = prev_node.next
        # point prev_node's next to the new new node
        prev_node.next = new_node
        return True

    def remove(self, target_data):
        """
        Removes the node in the list containing the target data. Returns
        false if target data not found.
        O(n) time, O(1) space.
        :param target_data:
        :return: False if target data not found.
        """
        # init nodes
        prev = None
        curr = self.head

        # move curr node to node holding target
        while curr is not None and curr.data != target_data:
            prev = curr  # advance previous pointer to sit with current pointer
            curr = curr.next  # continue traversal

        #
        if curr is not None:  # if curr is None, target not in list
            if curr is self.head:  # target was in the head, disconnect
                self.head = self.head.next
            else:
                prev.next = curr.next  # skip over target node
            return True
        return False  # not found

    def reverse(self):
        """
        Reverse a linkedlist from head to null.
        O(n) time, O(1) space.
        :return: New head pointer.
        """
        # init pointers
        prev = None
        curr = self.head
        next = None  # stored next pointer for reference

        while curr is not None:
            # save next
            next = curr.next  # where current is pointing in the orig direction
            curr.next = prev  # now reverse that sucker
            prev = curr  # move prev pointer over
            curr = next  # move next pointer over

        return prev  # new head

    def get_size(self):
        """
        Traverse the list from head to null and returns the size of the list.
        O(n) time, O(1) space.
        :return: size n of list
        """
        n = 0
        curr = self.head
        while curr is not None:
            n += 1
            curr = curr.next
        return n

    def find_node(self, target_val):
        """
        Performs unordered search of linked list given target value.
        O(n) time, O(1) space.
        :param target_val: Data to search for within node structs.
        :return: Node
        """
        curr = self.head
        while curr is not None and curr.data != target_val:
            curr = curr.next
        return curr is not None

    def find_middle_node(self):
        """
        Finds the middle node of the linked list, if even, returns the
        second middle element.
        O(n) time, O(1) space.
        :return: Data in the middle node.
        """
        # initialize slow and fast pointers
        slow = self.head
        fast = self.head

        # transversal until fast's next is null
        while fast and fast.next:
            slow = slow.next  # increment slow once
            fast = fast.next.next  # increment fast twice
        return slow.val

    def to_string(self):
        """
        Returns linked list data separated by arrow as string.
        O(n) time, O(1) space.
        :return: string
        """
        node = self.head
        while node is not None:
            print(node.data, "->", end='')
            node = node.next  # point to next node


if __name__ == '__main__':
    print("DEMO PUSH TO LINKEDLIST")
    print("Initializing empty Linked List...")
    my_list = LinkedList()
    print("Pushing 4 onto the list...")
    my_list.prepend(4)
    my_list.to_string()
    print("\nPushing 3 onto the list...")
    my_list.prepend(3)
    my_list.to_string()
    print("\nPushing 2 onto the list...")
    my_list.prepend(2)
    my_list.to_string()
    print("\nPushing 1 onto the list...")
    my_list.prepend(1)
    my_list.to_string()

    list = [1, 2, 3, 4]
    print("\n\nDEMO LINKEDLIST W/ LIST PARAM")
    my_other_list = LinkedList(list)
    my_other_list.to_string()
    print("\n Reverse")
    my_other_list.reverse()
    my_other_list.to_string()
