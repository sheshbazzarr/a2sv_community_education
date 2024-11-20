# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(10,head)  # Dummy node to simplify edge cases
        curr = dummy.next  # Start with the actual head of the list
        
        while curr is not None and curr.next is not None:  # Traverse while both curr and curr.next exist
            if curr.val == curr.next.val:  # If duplicate is found
                curr.next = curr.next.next  # Skip the duplicate
            else:
                curr = curr.next  # Move to the next node
        
        return head # Return the updated list
