/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function deleteDuplicates(head: ListNode | null): ListNode | null {

    if (head === null) return null
    else if (head.next === null) return head

    let currentNode = head
    let nextNode = head.next


    while (nextNode !== null) {
        if (currentNode.val === nextNode.val) {
            currentNode.next = null
            nextNode = nextNode.next
        } else {
            currentNode.next = nextNode
            currentNode = nextNode
            nextNode = currentNode.next
        }
    }

    return head
};