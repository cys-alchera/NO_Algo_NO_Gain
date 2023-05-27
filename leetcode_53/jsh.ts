function maxSubArray(nums: number[]): number {
    let max = nums[0]
    let previos = nums[0]

    for (let i = 1; i < nums.length; i++) {
        const crt = nums[i];

        previos = Math.max(previos + crt, crt);

        max = Math.max(previos, max);
    }
    return max
};

// Runtime 98ms Beats 17.90%
// Memory 52.6MB Beats 36.60%