# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        first = second = dummy_node

        # Move `second` to the k-th node from the start
        for _ in range(k):
            second = second.next

        # `temp` reaches the end, while `first` moves to find the k-th node from the end
        temp = second
        while temp.next:
            temp = temp.next
            first = first.next

        # Swap the values of the k-th nodes from start and end
        second.val, first.next.val = first.next.val, second.val

        return dummy_node.next
