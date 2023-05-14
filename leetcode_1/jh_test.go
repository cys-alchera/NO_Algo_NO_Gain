package leetcode_1

import (
	"testing"

	"github.com/go-playground/assert/v2"
)

func TestTwoSum(t *testing.T) {
	assert.Equal(t, twoSum([]int{2, 7, 11, 15}, 9), []int{0, 1})
	assert.Equal(t, twoSum([]int{3, 2, 4}, 6), []int{1, 2})
	assert.Equal(t, twoSum([]int{1, 1}, 3), []int{})
}
