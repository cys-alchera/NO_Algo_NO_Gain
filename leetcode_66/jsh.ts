function plusOne(digits: number[]): number[] {
    return (BigInt(digits.join('')) + 1n).toString().split('').map(v => Number(v))
};

// Runtime 72ms Beats 14.36% 
// Memory 44.3MB Beats 29.85%