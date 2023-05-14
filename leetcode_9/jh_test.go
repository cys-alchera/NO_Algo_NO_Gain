package leetcode_9

import (
	"testing"

	"github.com/go-playground/assert/v2"
)

func Test_isPalindrome(t *testing.T) {
	assert.Equal(t, isPalindrome(121), true)
	assert.Equal(t, isPalindrome(-121), false)
	assert.Equal(t, isPalindrome(10), false)
}
