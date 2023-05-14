package leetcode_2

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// https://leetcode.com/problems/add-two-numbers/
// Runtime 3ms Beats 98.8% Memory 4.6 MB Beats 87.88%
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	overFlowFlag := false
	newListNode := new(ListNode)
	current := newListNode
	for {
		sum := getNodeVal(l1) + getNodeVal(l2)
		if overFlowFlag {
			sum += 1
			overFlowFlag = false
		}

		if sum >= 10 {
			sum = sum % 10
			overFlowFlag = true
		}
		current.Val = sum

		l1 = getNext(l1)
		l2 = getNext(l2)

		if isNil(l1, l2) && !overFlowFlag {
			break
		}

		current.Next = new(ListNode)
		current = current.Next
	}

	return newListNode
}

func getNext(node *ListNode) *ListNode {
	if node == nil {
		return nil
	}
	return node.Next
}

func getNodeVal(node *ListNode) int {
	if node == nil {
		return 0
	}

	return node.Val
}

func addTwoNumbersVersion2(l1 *ListNode, l2 *ListNode) *ListNode {
	overFlowFlag := false
	newListNode := new(ListNode)
	current := newListNode
	for {
		sum := 0
		if isNotNil(l1) {
			sum += l1.Val
			l1 = l1.Next
		}

		if isNotNil(l2) {
			sum += l2.Val
			l2 = l2.Next
		}

		if overFlowFlag {
			sum += 1
			overFlowFlag = false
		}

		if sum >= 10 {
			sum = sum % 10
			overFlowFlag = true
		}
		current.Val = sum

		if isNil(l1, l2) && !overFlowFlag {
			break
		}

		current.Next = new(ListNode)
		current = current.Next
	}

	return newListNode
}

func isNil(nodes ...*ListNode) bool {
	for _, node := range nodes {
		if node != nil {
			return false
		}
	}
	return true
}

func isNotNil(nodes ...*ListNode) bool {
	return !isNil(nodes...)
}
