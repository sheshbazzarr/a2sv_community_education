# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None  # If there's one or no node, return None

        dummy = ListNode(0, head)  # Create a dummy node to handle edge cases
        slow = dummy  # `slow` will track the node before the middle
        fast = head   # `fthe ast` will help find middle node

        # Move `fast` pointer two steps and `slow` pointer one step
        while fast and fast.next:
            slow = slow.next  # Move slow to the node before the middle
            fast = fast.next.next  # Move fast two steps

        # Now, `slow.next` is the middle node, so skip it
        slow.next = slow.next.next  # Remove the middle node

        return dummy.next  # Return the updated list, starting from dummy.next
