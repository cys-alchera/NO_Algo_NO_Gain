"""
2023-05-27
LeeetCode 203. Remove Linked List Elements
Park Hee Chan
https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # head
        # prev = head
        # head.next.val == val
        # -> head.next = head.next.next

        mem = ListNode()
        mem.next = head
        prev = mem
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
                continue

            prev = prev.next

        return mem.next


'''
Runtime 77 ms
Beats 52.19%

Memory 19.9 MB
Beats 44.22%
'''