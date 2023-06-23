function addBinary(a: string, b: string): string {
    const reversedA = a.split('').reverse()
    const reversedB = b.split('').reverse()

    let index = 0
    let up = 0
    let answer = ''
    const endIndex = a.length > b.length ? a.length : b.length


    while (index < endIndex) {
        const aValue = reversedA[index] ? Number(reversedA[index]) : 0
        const bValue = reversedB[index] ? Number(reversedB[index]) : 0
        const add = aValue + bValue + up
        if (add >= 2) {
            answer = `${add - 2}` + answer
            up = 1
        } else {
            answer = `${add}` + answer
            up = 0
        }
        index++
    }
    if (up === 1) answer = '1' + answer
    return answer
};

// Runtime 74ms Beats 40.88%
// Memory 44.5MB Beats 88.87%