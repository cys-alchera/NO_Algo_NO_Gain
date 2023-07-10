function removeElement(nums: number[], val: number): number {
    let k = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === val) nums[i] = Infinity
        else k++
    }

    nums.sort((a, b) => {
        if (a == Infinity) return 1
        else if (b == Infinity) return -1
        else 0
    })

    return k
};

// Runtime 65ms Beats 51.89%
// Memory 44.3MB Beats 49.83%