# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        next = head.next
        head.next = None
        return self.aux(next, head)

    def aux(self, tail: Optional[ListNode], flippedHead: Optional[ListNode]) -> Optional[ListNode]:
        if not tail:
            return flippedHead
        next = tail.next
        tail.next = flippedHead
        return self.aux(next, tail)