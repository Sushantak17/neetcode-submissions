# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        # finding the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing the 2nd half of array
        prev = None
        curr = slow
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        # iterating using two pointers one from starting and one from end
        h1 = head
        h2 = prev
        while h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True

        