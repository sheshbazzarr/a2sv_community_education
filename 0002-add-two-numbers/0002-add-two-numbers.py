# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        list_start =dummy
        carry =0
        while l1 or l2 or carry:
            val1 =l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value =val1+val2+carry
            # carry is greater than 10 
            carry=value//10
            value=value%10
            # updater
            list_start.next=ListNode(value)

            # update pointers
            list_start =list_start.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
            
