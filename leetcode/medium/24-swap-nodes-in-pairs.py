# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy

        while temp.next and temp.next.next:
            first = temp.next
            second = temp.next.next

            # swap
            first.next = second.next
            second.next = first
            temp.next = second

            # move temp forward
            temp = first

        return dummy.next
