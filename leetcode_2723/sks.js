/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  return Promise.all([promise1, promise2]).then((values) => {
    return values.reduce(
      (acc, curr) => acc + curr, 0
    )
  })
};

// Runtime 62ms Beats 81.95%
// Memory 42.3MB Beats 15.43%
