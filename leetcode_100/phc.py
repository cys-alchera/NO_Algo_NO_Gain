"""
2023.05.09
Same Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            if p.val != q.val:
                return False

            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True

        if p is None and q is None:
            return True


'''
maybe recursive method was slow
Runtime Beats: 12.69% 44ms
Memory Beats: 7.15% 16.3MB
'''