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

function maxDepth(root: TreeNode | null): number {
  if (root === null) return 0;

  let max = 0;

  const dfs = (node: TreeNode, depth) => {
    if (depth > max) max = depth;
    if (node && node.left !== null) {
      dfs(node.left, depth + 1);
    }
    if (node && node.right !== null) {
      dfs(node.right, depth + 1);
    }
  };

  dfs(root, 1);

  return max;
}

// Runtime 77ms Beats 38.10%
// Memory 45.7MB Beats 99.47%
