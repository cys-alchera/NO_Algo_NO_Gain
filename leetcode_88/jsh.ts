/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    nums1.splice(m, nums1.length - m)
    nums2.splice(n)

    nums1.push(...nums2)
    nums1.sort((a, b) => a - b)
};
// 88. Merge Sorted Array
// Runtime 65ms Beats 55.77%
// Memory 43.9MB Beats 87.43%