package leetcode_9

// Runtime 12ms Beats 94.46%  Memory 4.3MB Beats 99.96%
// https://leetcode.com/problems/palindrome-number/description/
func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	reversed := reverseInt(x)
	return x == reversed
}

func reverseInt(num int) int {
	reversed := 0
	for num != 0 {
		remainder := num % 10
		reversed = reversed*10 + remainder
		num /= 10
	}
	return reversed
}
