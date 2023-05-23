// Runtime: 50 ms Beats 78.43%
// Memory: 7.4 MB Beats 78.43%
package find_all_duplicates_in_an_array

func findDuplicates(nums []int) []int {
	var count []int

	abs := func(x int) int {
		if x > 0 {
			return x
		}
		return -x
	}

	for i := range nums {
		idx := abs(nums[i]) - 1
		if nums[idx] > 0 {
			nums[idx] *= -1
		} else {
			count = append(count, abs(nums[i]))
		}
	}

	return count
}
