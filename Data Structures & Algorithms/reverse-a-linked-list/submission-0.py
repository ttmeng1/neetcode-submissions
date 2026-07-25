# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self = head
        prev = None
        while self is not None:
            temp = self.next
            self.next = prev
            prev = self
            self = temp
        return prev