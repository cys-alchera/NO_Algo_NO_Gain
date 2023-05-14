function isPalindrome(x: number): boolean {
    return String(x) === String(x).split('').reverse().join('')
};

// (Runtime 162ms, beats 94.5%, Memory 52.7mb, beats 15.5%)
