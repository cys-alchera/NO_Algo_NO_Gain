"""
2023-05-27
876. Middle of the Linked List
Park Hee Chan
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mem = head
        count = 0
        while mem:
            mem = mem.next
            count += 1

        point = count // 2 + 1

        mem_count = 1
        mem = head
        while mem:
            print(mem_count)
            if mem_count == point:
                return mem

            mem = mem.next
            mem_count += 1


"""
Runtime 48 ms
Beats 22.10%

Memory 16.3 MB
Beats 8.67%
"""