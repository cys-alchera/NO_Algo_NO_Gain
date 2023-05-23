package sum_root_to_leaf_numbers

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_sumNumbers(t *testing.T) {
	// given
	root := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 9,
			Left: &TreeNode{
				Val:   5,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val:   1,
				Left:  nil,
				Right: nil,
			},
		},
		Right: &TreeNode{
			Val:   0,
			Left:  nil,
			Right: nil,
		},
	}

	// when
	result := sumNumbers(root)

	// then
	assert.Equal(t, result, 1026)
}
