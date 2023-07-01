function mySqrt(x: number): number {
    if (x === 0) return 0
    if (x < 4) return 1
    if (x >= 4 && x < 9) return 2

    let max = x
    let min = 0

    while (min < max - 1) {
        const half = Math.floor((max + min) / 2)
        if (half * half === x) return half
        else if (half * half > x) max = half
        else min = half
    }

    return min
};

// Runtime 67ms Beats 90.38%
// Memory 45MB Beats 55.62%