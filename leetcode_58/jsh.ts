function lengthOfLastWord(s: string): number {
    const reg = new RegExp(/[\s]+/, 'g')
    const splitted = s.split(reg)
    for (let i = splitted.length - 1; i >= 0; i--) {
        if (splitted[i] !== '') return splitted[i].length
    }
    return 1
};

// Runtime 64ms Beats 47.55%
// Memory 44.1MB Beats 28.8%