"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity O(n)
    # Space Complexity O(1)
    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = None

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoListsRecursive(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeTwoListsRecursive(l1, l2.next)

        return temp

    def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        if l2 is not None:
            dummy.next = l2
        if l1 is not None:
            dummy.next = l1

        return head.next