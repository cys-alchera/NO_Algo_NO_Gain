"""
2023-05-27
206. Reverse Linked List
Park Hee Chan
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # node ( node (node (node ())))

        new_head = None
        prev = head
        while prev:
            mem = prev.next
            prev.next = new_head
            new_head = prev
            prev = mem

        return new_head


"""
Runtime 53 ms
Beats 28.14%

Memory 17.9 MB
Beats 26.81%
"""