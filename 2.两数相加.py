# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rtype = ListNode()
        first = rtype
        carry = 0
        while (True):
            rval = l1.val + l2.val + carry
            if rval < 10 :
                carry = 0
                rtype.val = rval
            else:
                carry = int(rval / 10)
                rtype.val = rval % 10 
            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 != None:
                l1 = ListNode()
            elif l1 != None and l2 == None:
                l2 = ListNode()
            elif l1 == None and l2 == None:
                if carry != 0:
                    rtype.next = ListNode(carry)
                break
            rtype.next = ListNode()
            rtype = rtype.next


        
l1 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)
l1.next = l11
l11.next = l12

l2 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)
l2.next = l21
l21.next = l22

s = Solution()
s.addTwoNumbers(l1,l2)