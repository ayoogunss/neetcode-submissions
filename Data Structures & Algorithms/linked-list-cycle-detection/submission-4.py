# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        cur1 = head
        cur2 = head.next
        while(cur1 != None and cur1.next != None and cur2 != None and cur2.next != None):
            if cur1 == cur2:
                return True
            cur1 = cur1.next
            cur2 = cur2.next.next
        return False