# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            #storing the next node
            next_node = curr.next
            #changing the pointers
            curr.next = prev

            #Resetting the prev and current nodes for future iterations
            prev = curr
            curr = next_node
        
        return prev
            