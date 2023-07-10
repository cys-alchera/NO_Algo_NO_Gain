function removeDuplicates(nums: number[]): number {
    const set = new Set()
    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i])) nums[i] = Infinity
        else set.add(nums[i])
    }
    nums.sort((a, b) => a - b)
    return set.size
};

// Runtime 87ms Beats 36.53%
// Memory 48.2MB Beats 5.65%