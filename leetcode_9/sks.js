/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  return x.toString() === x.toString().split('').reverse().join('')
};

// Memory 51.6MB Beats 29.20%
// Runtime 180ms Beats 54.23%
