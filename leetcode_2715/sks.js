/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
  let cancel = false
  setTimeout(() => {
    if (!cancel) {
      fn(...args)
    }
  }, t)
  return function cancelFn() {
    cancel = true
  }
};

// Runtime 68ms Beats 67.90%
// Memory 42.3MB Beats 28.49%
