# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.length(head)
        newN = l - n
        return self.aux(head, newN)
    
    def aux(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head.next
        rest = self.aux(head.next, n - 1)
        head.next = rest
        return head

    def length(self, head: Optional[ListNode]) -> int:
        if head == None: return 0
        return 1 + self.length(head.next)