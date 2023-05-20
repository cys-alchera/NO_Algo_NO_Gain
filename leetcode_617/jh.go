package jh

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Runtime 10ms Beats94.96% Memory7.2 MBBeats 68.91%
func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil && root2 == nil {
		return nil
	}

	newNode := &TreeNode{}
	if root1 != nil {
		newNode.Val += root1.Val
	}

	if root2 != nil {
		newNode.Val += root2.Val
	}

	newNode.Left = mergeTrees(getLeft(root1), getLeft(root2))
	newNode.Right = mergeTrees(getRight(root1), getRight(root2))
	return newNode
}

func getLeft(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	return node.Left
}

func getRight(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	return node.Right
}
