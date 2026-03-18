# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        t1, t2 = list1, list2
        while t1 and t2:
            if t1.val <= t2.val:
                curr.next = t1
                curr = curr.next
                t1 = t1.next
            else:
                curr.next = t2
                curr = curr.next
                t2 = t2.next
        if t1:
            curr.next = t1
        elif t2:
            curr.next = t2
        return dummy.next
