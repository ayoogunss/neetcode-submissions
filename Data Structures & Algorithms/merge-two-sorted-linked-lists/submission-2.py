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
        if(list1.val <= list2.val):
            list3 = list1
            list1 = list1.next
        else:
            list3 = list2
            list2 = list2.next
        cur = list3
        while(list1 != None and list2 != None):
            if(list1.val <= list2.val):
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        while(list1 != None):
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        while(list2 != None):
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        return list3