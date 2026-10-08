# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        cur1 = list1
        cur2 = list2
        if cur1.val <= cur2.val:
            list3 = cur1
            cur1 = cur1.next
            tail = list3
        else:
            list3 = cur2
            cur2 = cur2.next
            tail = list3
        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                list3.next = cur1
                cur1 = cur1.next
            else:
                list3.next = cur2
                cur2 = cur2.next
            list3 = list3.next
        while(cur2 != None):
            list3.next = cur2
            cur2 = cur2.next
            list3 = list3.next
        while(cur1 != None):
            list3.next = cur1
            cur1 = cur1.next
            list3 = list3.next
        return tail