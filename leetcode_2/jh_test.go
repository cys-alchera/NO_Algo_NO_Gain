package leetcode_2

import (
	"testing"

	"github.com/go-playground/assert/v2"
)

func TestAddTwoNumbers(t *testing.T) {
	t1ListNode := addTwoNumbers(arrayToListNode([]int{5, 6, 4}), arrayToListNode([]int{2, 4, 3}))
	assert.Equal(t, listNodeToIntArray(t1ListNode), []int{7, 0, 8})

	t2ListNode := addTwoNumbers(arrayToListNode([]int{9, 9, 9, 9, 9, 9, 9}), arrayToListNode([]int{9, 9, 9, 9}))
	assert.Equal(t, listNodeToIntArray(t2ListNode), []int{8, 9, 9, 9, 0, 0, 0, 1})
}

func listNodeToIntArray(listNode *ListNode) []int {
	numbers := []int{}
	current := listNode
	for {
		if current == nil {
			break
		}
		numbers = append(numbers, current.Val)
		current = current.Next
	}

	return numbers
}

func arrayToListNode(numbers []int) *ListNode {
	root := new(ListNode)
	current := root
	index := 0
	for {
		current.Val = numbers[index]
		index++
		if index == len(numbers) {
			break
		}
		current.Next = new(ListNode)
		current = current.Next

	}
	return root
}
