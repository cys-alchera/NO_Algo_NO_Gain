/**
 * @param {string} num
 * @return {string}
 */
var removeTrailingZeros = function (num) {
  return num.replace(/0+$/, "");
};

// Runtime 80ms Beats 24.29%
// Memory 44.4MB Beats 87.71%
