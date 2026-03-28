# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length: int = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length == 1:
            return None
        if length - n == 0:
            return head.next

        currlen: int = 0
        temp = head
        while temp:
            currlen += 1
            if currlen == length - n:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
