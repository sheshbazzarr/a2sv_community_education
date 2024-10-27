from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize dummy node pointing to head
        dummy_node = ListNode(0, head)
        
        # Step 1: Find the k-th node from the beginning using `second`
        first = second = dummy_node
        for _ in range(k):
            second = second.next  # Move `second` to the k-th node
        # `first` will be used later to find the k-th node from the end

        # Save the reference to the k-th node from the start
        kth_from_start = second

        # Step 2: Use `temp` to traverse to the end, and move `first` along to find the k-th node from the end
        temp = second
        while temp.next:
            temp = temp.next
            first = first.next

        # `first` is now pointing to the node before the k-th node from the end
        kth_from_end = first.next

        # Step 3: Swap the values of the two nodes
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        # Return the original head, which is `dummy_node.next`
        return dummy_node.next
