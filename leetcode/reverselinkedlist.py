# runtime complexity: O(n)
# spacetime complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:      
        prev_node = None # represent the end
        curr_node = head # current node in list
        while curr_node:
            next_node = curr_node.next # temp node for the rest of the list
            curr_node.next = prev_node # update current next to the end
            prev_node = curr_node # update previous node
            curr_node = next_node # update current node
        head = prev_node
        return head
        
