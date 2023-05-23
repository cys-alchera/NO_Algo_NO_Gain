package same_tree

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_isSameTree(t *testing.T) {
	t.Run("OK", func(t *testing.T) {
		// given
		p := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}
		q := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}

		// when
		result := isSameTree(p, q)

		// then
		assert.Equal(t, result, true)
	})
}
