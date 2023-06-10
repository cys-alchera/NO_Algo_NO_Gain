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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const list1Head = list1?.val
    const list2Head = list2?.val

    if (list1Head === undefined && list2Head === undefined) return null
    else if (list1Head !== undefined && list2Head === undefined) return list1
    else if (list1Head === undefined && list2Head !== undefined) return list2

    const answer = {
        head: null,
        tail: null
    }
    let left1 = null
    let left2 = null

    if (list1Head <= list2Head) {
        answer.head = list1
        answer.tail = list1
        left1 = list1.next
        left2 = list2
    } else {
        answer.head = list2
        answer.tail = list2
        left1 = list1
        left2 = list2.next
    }

    answer.tail.next = null
    while (left1?.val !== undefined || left2?.val !== undefined) {
        const head1 = left1?.val
        const head2 = left2?.val

        if (head1 !== undefined && head2 === undefined || head1 <= head2) {
            answer.tail.next = left1
            answer.tail = left1
            left1 = left1.next
        } else if (head1 === undefined && head2 !== undefined || head1 > head2) {
            answer.tail.next = left2
            answer.tail = left2
            left2 = left2.next
        }
        answer.tail.next = null
    }
    return answer.head
};

// Runtime 74ms Beats 46.70%
// Memory 45.3MB Beats 26.31%