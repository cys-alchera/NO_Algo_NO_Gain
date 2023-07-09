/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
  const arrayLength = arr.length
  for (let i = 0; i < arrayLength; i++) {
    arr[i] = fn(arr[i], i)
  }
  return arr;
};

// Runtime 72ms Beats 5.53%
// Memory 42.1MB Beats 40.27%
