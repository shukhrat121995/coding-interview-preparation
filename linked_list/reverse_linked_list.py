"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Iterative:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


class Recursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

