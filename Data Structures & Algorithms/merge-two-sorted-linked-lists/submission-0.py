# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1) # create fake node
        prev = prehead 

        while list1 and list2: # traverse through shorter list
            # find smaller node
            if list1.val < list2.val:
                prev.next = list1 # make smaller node the next node
                list1 = list1.next # iterate through list of smaller node
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next # move pointer up

        # append list that still has nodes left
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        
        return prehead.next
