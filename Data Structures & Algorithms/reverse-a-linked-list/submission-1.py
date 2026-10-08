# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur != None:
            # make a variable to store the next node
            curnext = cur.next
            # assign next node to prev
            cur.next = prev
            # move previous to the cur
            prev = cur
            # now move cur to the next node
            cur = curnext
        return prev