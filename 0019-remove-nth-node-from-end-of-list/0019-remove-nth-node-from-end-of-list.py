# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        first=second=dummy_node
        for _ in range(1,n+1):
            first=first.next
        while first.next is not None:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy_node.next
            