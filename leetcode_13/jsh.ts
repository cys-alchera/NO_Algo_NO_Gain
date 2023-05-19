const ROMAN = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
}

function romanToInt(s: string): number {
    let answer = 0
    const symbols = s.split('')
    const len = symbols.length

    for (let i = 0; i < len; i++) {
        if (len - 1 > i && ROMAN[symbols[i]] < ROMAN[symbols[i + 1]]) {
            answer += (ROMAN[symbols[i + 1]] - ROMAN[symbols[i]])
            i += 1
            continue
        }
        answer += ROMAN[symbols[i]]
    }

    return answer
};

  // Runtime 128ms, beats 77.71%, Memory 47.6mb, beats 93.20%