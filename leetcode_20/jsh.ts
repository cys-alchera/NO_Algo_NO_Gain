function isValid(s: string): boolean {
    const braket = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    const stack = []

    for (let i = 0; i < s.length; i++) {
        const latest = stack[stack.length - 1]
        if (braket[latest] === s[i]) stack.pop()
        else stack.push(s[i])
    }

    return stack.length === 0 ? true : false
};

// Runtime 63ms Beats 79.7% Memory 44.7MB Beats 58.21%