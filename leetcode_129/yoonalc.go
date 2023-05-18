// Runtime: 2ms, Beats 63.71%
// Memory: 2.2MB, Beats 78.23%

package sum_root_to_leaf_numbers

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumNumbers(root *TreeNode) int {
	var (
		sum = 0
	)

	var dfs func(node *TreeNode, valPath int)
	dfs = func(node *TreeNode, valPath int) {
		valPath *= 10
		valPath += node.Val

		if node.Left == nil && node.Right == nil {
			sum += valPath
			return
		}

		dfs(node.Left, valPath)
		dfs(node.Right, valPath)
	}

	dfs(root, 0)

	return sum
}
