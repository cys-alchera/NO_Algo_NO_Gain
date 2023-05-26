// Runtime: 1 ms Beats 64.73%
// Memory: 2 MB Beats 99.61%
package main

import (
	"strconv"
	"strings"
)

func decodeString(s string) string {
	var (
		stack  []string
		length = len(s)
	)

	for idx := 0; idx < length; idx++ {
		v := string(s[idx])
		switch v {
		case "]":
			// pop
			var word string
			var num string

			// alphabet
			popped := stack[len(stack)-1]
			for len(stack) > 0 {
				popped = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if popped == "[" {
					break
				}
				word = popped + word
			}

			// number
			for len(stack) > 0 {
				popped = stack[len(stack)-1]
				if !(popped >= "0" && popped <= "9") {
					break
				}
				stack = stack[:len(stack)-1]
				num = popped + num
			}

			multiple, _ := strconv.Atoi(num)
			stack = append(stack, strings.Repeat(word, multiple))
		default:
			stack = append(stack, v)
		}
	}

	return strings.Join(stack, "")
}
