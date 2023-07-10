/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function inorderTraversal(root: TreeNode | null): number[] {
    const answer = []
    function dfs(node) {
        if (node?.left) dfs(node.left)
        if (node?.val || node?.val === 0) answer.push(node.val)
        if (node?.right) dfs(node.right)
    }
    dfs(root)
    return answer
};

// Runtime 68ms Beats 34.72%
// Memory 44.1MB Beats 87.86%