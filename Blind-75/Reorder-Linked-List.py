# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rev(head) -> Optional[ListNode]:
            prev = nxt = None
            temp = head
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            return prev

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        firhead = head
        sechead = rev(slow.next)
        dummy = ListNode()
        curr = dummy
        t1, t2 = firhead, sechead
        while t1 and t2:
            curr.next = t1
            curr = curr.next
            t1 = t1.next
            curr.next = t2
            curr = curr.next
            t2 = t2.next
        if t1:
            curr.next = t1
        elif t2:
            curr.next = t2
        return dummy.next
