"""
234 Palindrome Linked List
Lee SooHyung
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward, Double_forward = head, head
        backward = None
        while Double_forward and Double_forward.next:
            Double_forward = Double_forward.next.next
            backward, backward.next, forward = forward, backward, forward.next
        # 전체 길이가 홀수일 경우
        if Double_forward:
            forward = forward.next
        while forward:
            if forward.val == backward.val:
                forward = forward.next
                backward = backward.next
            else:
                return False
        return True

'''
RESULT
Runtime 641ms, 99.8% beats
Memory 33.6MB, 93.69% beats
'''
