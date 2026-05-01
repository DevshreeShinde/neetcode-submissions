# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        count=head
        nodecount = 0
        while count:
            count =count.next
            nodecount+=1

        # remove head case
        if nodecount == n:
            return head.next

        removen = nodecount-n-1
        count=head
        while removen:
            count=count.next
            removen-=1
        count.next=count.next.next
        return head