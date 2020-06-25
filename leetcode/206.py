# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative way from solution
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
        # My iterative way
        if not head or not head.next:
            return head
        fir, sec = head, head.next
        head.next = None
        while sec:
            # WRONG!!! -- fir, sec, sec.next = sec, sec.next, fir
            nfir, nsec = sec, sec.next
            sec.next = fir
            fir, sec = nfir, nsec
        return fir
        # Recursive way
        if not head or not head.next:
            return head
        tail = head.next
        res = self.reverseList(head.next)
        tail.next, head.next = head, None
        return res
