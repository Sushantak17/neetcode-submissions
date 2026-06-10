# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if list has only 1 or 2 nodes
        if not head.next or not head.next.next:
            return
        # split
        mid = end = head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        p2 = mid.next
        mid.next = None
    
        # reverse
        prev = None
        while p2 and p2.next:
           p2_next = p2.next
           p2.next = prev
           prev = p2
           p2 = p2_next
        p2.next = prev

        # merge
        p1 = head
        while p2:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next

