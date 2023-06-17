// Runtime: 0 ms Beats 100%
// Memory: 1.9 MB Beats 78.13%

package leetcode_1859

import (
	"strconv"
	"strings"
)

func sortSentence(s string) string {
	splited := strings.Split(s, " ")

	arr := make([]string, len(splited))
	for _, word := range splited {
		last := len(word) - 1
		idx, _ := strconv.Atoi(string(word[last]))
		arr[idx-1] = word[:last]
	}

	return strings.Join(arr, " ")
}
