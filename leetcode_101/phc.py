"""
2023-05-20
Leetcode 101: Symmetric Tree
Park Hee Chan

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True

        # if p and q 로 하면 runtime 속도가 더 느려지는 현상이 발생...?!!
        if p is not None and q is not None:
            if p.val != q.val:
                return False

            if self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left):
                return True


'''
Runtime 43 ms
Beats 38.42%
Memory 16.5 MB
Beats 9.95%
'''