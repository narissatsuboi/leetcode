"""
Given the head of a singly linked list, return true if it is a palindrome.
Clarify - LL does not need to keep its order.
Input - Head of sll.
Output - True if palindrome.
Big Picture - Half 1 of LL should match the reverse of Half 2 if palindrome.
Can use slow and fast pointers to split a list by the middle, where fast is
always 2x ahead of slow.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None: # empty list is palindrome
            return True

        slow, fast = head, head
        # 1 Find middle node of ll. Set as head to 2nd half of list.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next  # x2 jumps
        first_half_end = slow  # store end loc of start of other half
        # 2 Reverse the second half
        second_half_start = self.reverse(first_half_end.next)
        # 3 Iterate both halves, if data doesn't match, False.
        first_head = head
        second_head = second_half_start
        result = True
        while result and second_half_start is not None:
            # check for non palindromic condition
            if first_head.val != second_head.val:
                result = False
            # continue traversal
            first_head = first_head.next
            second_head = second_head.next
        # 4 Restore the list to orig order
        first_half_end.next = self.reverse(second_half_start)
        return result

    def reverse(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


if __name__ == '__main__':
    print("")
