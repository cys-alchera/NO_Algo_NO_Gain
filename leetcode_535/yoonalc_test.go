package leetcode_535

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_Codec(t *testing.T) {
	t.Run("url encode -> decode == origin url", func(t *testing.T) {
		// given
		var (
			url      = "https://leetcode.com/problems/design-tinyurl"
			expected = "https://leetcode.com/problems/design-tinyurl"
		)

		// when
		obj := Constructor()
		tiny := obj.encode(url)
		answer := obj.decode(tiny)

		// then
		assert.Equal(t, answer, expected)
	})
}
