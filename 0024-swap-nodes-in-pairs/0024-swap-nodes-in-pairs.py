# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node =ListNode(0,head)
        previous_node ,current_node = dummy_node, head

        while current_node is not None and current_node.next is not None:
            #  save pointers to the next pair
            next_pair = current_node.next.next
            second_node = current_node.next

            # reverse the current pair 
            second_node.next = current_node
            current_node.next = next_pair
            previous_node.next= second_node

            # update pointers to the next iteration 
            previous_node = current_node
            current_node = next_pair
        return dummy_node.next
        