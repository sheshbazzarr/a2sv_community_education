# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node=ListNode(0,head)
        current=dummy_node
        while current.next  is not None:
            if current.next.val==val:
                current.next =current.next.next
            else:
                current=current.next
        return dummy_node.next