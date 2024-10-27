# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the kth node from the beginning
        first = head
        for _ in range(k - 1):
            first = first.next

        # Step 2: Find the kth node from the end using two pointers
        second = head
        temp=first
        while temp.next is not None:
            temp = temp.next
            second = second.next

        # Step 3: Swap the values of the two nodes
        first.val, second.val = second.val, first.val

        # Return the modified list
        return head