# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        ret = head

        carry = 0
        while l1 or l2 or carry != 0: 
            res = 0

            if l1 and l2:
                res = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res = l1.val + carry
                l1 = l1.next
            elif l2:
                res = l2.val + carry
                l2 = l2.next
            else:
                res = 1

            if res >= 10:
                carry = 1
                res -= 10
            else:
                carry = 0

            dummy = ListNode(res, None)
            head.next = dummy
            head = head.next 

        return ret.next