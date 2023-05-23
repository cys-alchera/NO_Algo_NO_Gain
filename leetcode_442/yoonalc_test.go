package find_all_duplicates_in_an_array

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_findDuplicates(t *testing.T) {
	t.Run("OK", func(t *testing.T) {
		// given
		tcs := []struct {
			nums   []int
			output []int
		}{
			{[]int{4, 3, 2, 7, 8, 2, 3, 1}, []int{2, 3}},
			{[]int{1, 1, 2}, []int{1}},
		}
		for _, tc := range tcs {
			// when
			result := findDuplicates(tc.nums)

			// then
			assert.Equal(t, result, tc.output)
		}
	})
}
