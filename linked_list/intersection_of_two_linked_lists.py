"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node 8:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before
the intersected node in A; There are 3 nodes before the intersected node in B.


It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def length(self, node: ListNode) -> int:
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = self.length(headA)
        lengthB = self.length(headB)

        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1

        while lengthA < lengthB:
            headB = headB.next
            lengthB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
