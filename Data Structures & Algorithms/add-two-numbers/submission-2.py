# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currNode = ListNode()
        toRet = currNode
        nextNode = None
        carry = 0
        while l1 != None or l2 != None or carry != 0:

            val1 = 0 if l1 == None else l1.val
            val2 = 0 if l2 == None else l2.val
            currNode.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next

            nextNode = ListNode()
            currNode.next = nextNode
            nextNode = currNode
            currNode = currNode.next

        if nextNode.next.val == 0:
            nextNode.next = None

        return toRet