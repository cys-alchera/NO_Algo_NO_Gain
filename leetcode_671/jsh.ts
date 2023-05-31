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

function findSecondMinimumValue(root: TreeNode | null): number {
    const smallest = root.val;
    const answer = [];

    function DFS(node) {
        if (node.left === null) return
        else {
            if (node.left.val > smallest) answer.push(node.left.val)
            if (node.right.val > smallest) answer.push(node.right.val)

            DFS(node.left)
            DFS(node.right)
        }
    }
    DFS(root)
    return answer.length == 0 ? -1 : Math.min(...answer)
};

// Runtime 65ms Beats 65.22%
// Memory 42.8MB Beats 82.61%