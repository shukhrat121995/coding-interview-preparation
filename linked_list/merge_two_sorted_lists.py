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
    # Time Complexity O(m) or O(n) depending on size of two linked lists, basically it will be the smallest size
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

# MORE ABOUT SPACE COMPLEXITY
"""
You are absolutely right that you are going to need Θ(n) storage space to hold the result of merging two lists of total 
length n. But how much of that storage space was already there before the function started running, and how much of that 
storage space is new? You already had two lists of n total elements, so you already were using Θ(n) space before you 
started this algorithm, and when you're done you have the same lists lying around, just rewired so that the next 
pointers might be pointing to different places. As a result, the amount of memory you needed to allocate for this 
procedure is not Θ(n), but rather Θ(1).

More generally, it's common when measuring space complexity to ignore the space used by the inputs to the problem, 
because in some sense that space cost is unavoidable and there's nothing you can do to eliminate it.

One piece of advice going forward: if you write something like O(1) or O(n), it's often a good idea to make clear 
whether you're measuring time or space. For example, it's clearer to say that the procedure needs O(n) memory or O(1) 
time rather than to say that the procedure "is" O(n) or "is" O(1), since it's unclear what you're measuring with 
the big-O notation when you do that.
"""