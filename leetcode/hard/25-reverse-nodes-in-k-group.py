# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k_nodes(curr, k):
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            return count == k

        def reverse_segment(segment_head, k):
            prev = None
            curr = segment_head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, segment_head  # new head, new tail

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while has_k_nodes(prev_group_tail.next, k):
            segment_head = prev_group_tail.next
            segment_tail = segment_head
            for _ in range(k - 1):
                segment_tail = segment_tail.next

            next_segment_head = segment_tail.next
            new_head, new_tail = reverse_segment(segment_head, k)
            prev_group_tail.next = new_head
            new_tail.next = next_segment_head
            prev_group_tail = new_tail

        return dummy.next
