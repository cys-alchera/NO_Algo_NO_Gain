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

function isSymmetric(root: TreeNode | null): boolean {
  if (root === null) return false;

  let queue = [[root.left, root.right]];

  while (queue.length) {
    const [lNode, rNode] = queue.shift();

    if (lNode?.val !== rNode?.val) return false;

    if (lNode !== null && rNode !== null) {
      queue.push([lNode.left, rNode.right]);
      queue.push([lNode.right, rNode.left]);
    }
  }

  return true;
}

// Runtime 68ms Beats 75.41%
// Memory 45.8MB Beats 10.25%
