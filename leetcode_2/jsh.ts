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

type queueType = {
    node1: ListNode | null
    node2: ListNode | null
    carry: Boolean
}
type makeNodeReturnType = {
    isExceed10: Boolean
    node: ListNode
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (l1 === null && l2 === null) return null

    const nodeList: Array<ListNode> = []

    const queue: Array<queueType> = [{
        node1: l1, node2: l2, carry: false,
    }]

    while (queue.length) {
        const { node1, node2, carry } = queue.shift()
        const node1Value = node1 ? node1.val : 0
        const node2Value = node2 ? node2.val : 0
        let sum = node1Value + node2Value
        if (carry) sum += 1

        const { node, isExceed10 } = makeNode(sum)
        nodeList.push(node)
        if (node1?.next || node2?.next) queue.push({ node1: node1?.next, node2: node2?.next, carry: isExceed10 })
        else if (isExceed10) nodeList.push(new ListNode(1))

    }

    for (let i = 0; i < nodeList.length - 1; i++) {
        nodeList[i].next = nodeList[i + 1]
    }

    return nodeList[0]
};

function makeNode(value): (makeNodeReturnType | null) {
    let isExceed10 = false
    const node = new ListNode(value % 10)
    if (value >= 10) isExceed10 = true
    return { node, isExceed10 }
}


// (Runtime 100ms, beats 84.2%, Memory 49mb, beats 25.73%)