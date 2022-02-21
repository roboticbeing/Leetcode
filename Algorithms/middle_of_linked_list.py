from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        count = 0
        start = node = head
        # get length
        while start:
            size += 1
            start = start.next

        mid = size // 2

        # get mid
        while node:
            if count == mid:
                return node
            else:
                count += 1
                node = node.next

    def middleNodeFastPointers(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

