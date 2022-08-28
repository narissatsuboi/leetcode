
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # use dummy Dummy -> 1 -> 2 -> 3 -> 4 -> 5
    dummy = ListNode(-1, head)

    # reach node at "left" position
    leftPrev = dummy
    curr = head
    for i in range(left - 1):
        leftPrev = curr   # stores where rightNode will point later
        curr = curr.next

    # reverse segment from left to right
    prev = None
    for i in range(right - left + 1):  # segment from left:right
        # same as reverse linked list problem
        tempNode = curr.next
        curr.next = prev
        prev = curr
        curr = tempNode

    # update pointers at end of ea segment
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next


if __name__ == '__main__':
    print()

    llist = ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                ListNode(5, None)))))

    curr = llist

    while curr:
        print(f"{curr.val} ->", end="")
        curr = curr.next
    print()

    reverseBetween(llist, 2, 4)

    curr = llist
    while curr:
        print(f"{curr.val} ->", end="")
        curr = curr.next

    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
