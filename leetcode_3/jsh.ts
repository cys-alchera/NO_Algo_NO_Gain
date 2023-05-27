type hashType = {
    [key: string | number]: number
}

function lengthOfLongestSubstring(s: string): number {
    let answer = 0
    let strLen = 0
    let startIndex = 0
    let hash: hashType = {}

    for (let i = 0; i < s.length; i++) {
        const prevCharIndex = hash[s[i]]
        if (prevCharIndex === undefined) {
            strLen++
            if (answer < strLen) answer = strLen
        } else {
            if (s[i] === s[i - 1]) {
                strLen = 1
                hash = {}
            } else {
                strLen = strLen - prevCharIndex + startIndex
                for (let j = startIndex; j <= prevCharIndex; j++) delete hash[s[j]]
            }
            startIndex = prevCharIndex + 1
        }
        hash[s[i]] = i
    }
    return answer
};

// Runtime 111 ms Beats 41.58% Memory 51.6 MB Beats 11.86%