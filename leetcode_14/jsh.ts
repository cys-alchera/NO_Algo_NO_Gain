function longestCommonPrefix(strs: string[]): string {
    let answer = ''

    for (let charIdx = 0; charIdx < strs[0].length; charIdx++) {
        const stand = strs[0][charIdx]
        console.log(stand, charIdx)
        if (!stand) return answer
        for (let strIdx = 1; strIdx < strs.length; strIdx++) {
            console.log(strs[strIdx][charIdx], charIdx, strIdx)
            if (stand !== strs[strIdx][charIdx]) {
                return answer
            }
        }
        answer += stand
    }
    return answer
};

// Runtime 66ms, beats 67.17%, Memory 44.8mb, beats 50.4%