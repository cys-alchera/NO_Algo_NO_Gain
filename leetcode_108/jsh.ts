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

function sortedArrayToBST(nums: number[]): TreeNode | null {
  if (nums.length === 0) return null;

  const queue = [];

  const nodeMaker = (arr) => {
    if (arr.length === 0) return null;

    const center = Math.floor(arr.length / 2);

    const left = arr.slice(0, center);
    const right = arr.slice(center + 1);
    const node = new TreeNode(arr[center]);

    queue.push({ node, left, right });

    return node;
  };

  let root = nodeMaker(nums);

  while (queue.length) {
    const { node, left, right } = queue.shift();

    node.left = nodeMaker(left);
    node.right = nodeMaker(right);
  }

  return root;
}

// Runtime 73ms Beats 76.34%
// Memory 46.1MB Beats 24.61%
