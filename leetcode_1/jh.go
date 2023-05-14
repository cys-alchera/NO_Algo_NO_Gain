package leetcode_1

// https://leetcode.com/problems/two-sum/
// Runtime 2ms Beats 96.59% Memory 4.2 MB Beats 59.44%
func twoSum(nums []int, target int) []int {
	numberOfIndex := make(map[int]int, len(nums))
	for index, number := range nums {
		unknown := target - number
		if v, exist := numberOfIndex[unknown]; exist {
			return []int{v, index}
		}
		numberOfIndex[number] = index
	}
	return []int{}
}
