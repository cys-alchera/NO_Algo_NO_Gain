function twoSum(nums: number[], target: number): number[] {
    const len = nums.length
    const obj = {}

    for (let i = 0; i < len; i++) {
        obj[nums[i]] = i
    }

    for (let i = 0; i < len; i++) {
        const rest = target - nums[i]
        if (obj[rest] && i !== obj[rest]) {
            return [i, obj[rest]]
        }
    }
    return []
};

// (Runtime 79ms, beats 53.26%, Memory 45.5mb, beats 27.06%)