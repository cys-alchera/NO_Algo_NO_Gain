function searchInsert(nums: number[], target: number): number {
    let answer = null
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= target) {
            answer = i
            break
        }
    }
    if (answer === null) return nums.length
    return answer
};

// Runtime 70ms Beats 25%
// Memory 45MB Beats 7.19%