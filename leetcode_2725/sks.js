/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
  fn(...args);
  let interval = setInterval(() => {
    fn(...args)
  }, t)
  let cancelFn = () => clearInterval(interval);
  return cancelFn
};

/**
 *  const result = []
 *
 *  const fn = (x) => x * 2
 *  const args = [4], t = 20, cancelT = 110
 *
 *  const start = performance.now()
 *
 *  const log = (...argsArr) => {
 *		const val = fn(...argsArr)
 *      result.push({"time": Math.floor(performance.now() - start), "returned": fn(...argsArr)})
 *  }
 *
 *  const cancel = cancellable(log, args, t);
 *
 *  setTimeout(() => {
 *     cancel()
 *     console.log(result) // [
 *                         //      {"time":0,"returned":8},
 *                         //      {"time":20,"returned":8},
 *                         //      {"time":40,"returned":8},
 *                         //      {"time":60,"returned":8},
 *                         //      {"time":80,"returned":8},
 *                         //      {"time":100,"returned":8}
 *                         //  ]
 *  }, cancelT)
 */

// Runtime 63ms Beats 90.20%
// Memory 42.5MB Beats 15.41%