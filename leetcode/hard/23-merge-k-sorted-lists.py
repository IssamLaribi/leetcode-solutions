# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        sorted = ListNode()

        index = 0
        for node in lists:
            while node:
                heapq.heappush(pq, (node.val, index, node))
                node = node.next
                index += 1 

        
        dummy = sorted
        while pq:
            val, idx, node = heapq.heappop(pq)   
            dummy.next = node                    
            dummy = dummy.next

        return sorted.next
