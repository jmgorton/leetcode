from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        lead = follow = head
        kd = k
        while kd:
            kd -= 1
            if lead.next: lead = lead.next
            else: 
                lead = head
                kd %= (k - kd)
        while lead.next:
            lead = lead.next
            follow = follow.next
        lead.next = head
        head = follow.next
        follow.next = None
        return head