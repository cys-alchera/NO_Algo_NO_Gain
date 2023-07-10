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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if (p === null && q === null) return true;
  else if ((p !== null && q === null) || (p === null && q !== null))
    return false;

  let answer = true;

  function DFS(node1: TreeNode | null, node2: TreeNode | null) {
    if (!answer) return;
    if (node1.val !== node2.val) answer = false;
    else {
      if (node1.left !== null && node2.left !== null)
        DFS(node1.left, node2.left);
      else if (
        (node1.left !== null && node2.left === null) ||
        (node1.left === null && node2.left !== null)
      )
        answer = false;
      if (node1.right !== null && node2.right !== null)
        DFS(node1.right, node2.right);
      else if (
        (node1.right !== null && node2.right === null) ||
        (node1.right === null && node2.right !== null)
      )
        answer = false;
    }
  }

  DFS(p, q);

  return answer;
}

// Runtime 69ms Beats 25.93%
// Memory 44.6MB Beats 51.46%
