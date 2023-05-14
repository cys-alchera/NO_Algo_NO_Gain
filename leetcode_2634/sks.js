/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  if (!arr) return [];
  let result = [];
  arr.forEach((item, index) => {
    if (fn(item, index)) result.push(item);
  });
  return result;
};

// Runtime 66 ms Beats 14.76%
// Memory 42MB Beats 52.31%
