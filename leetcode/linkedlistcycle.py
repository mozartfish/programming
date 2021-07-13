# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        1. keep track of the nodes that have been visited -> set
        2. loop through nodes looking for a cycle
        '''
        
        node_set = set()
        
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        
        return False
            