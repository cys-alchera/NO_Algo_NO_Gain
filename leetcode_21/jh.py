# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Runtime 51 ms Beats 35.52% Memory 16.4 MB Beats 19.46%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        current = new_list
        while self.is_not_none(list1) and self.is_not_none(list2):
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if self.is_not_none(list1):
            current.next = list1
        if self.is_not_none(list2):
            current.next = list2

        return new_list.next


    def is_not_none(self, elem: Optional[ListNode]) -> bool :
        return elem is not None
    