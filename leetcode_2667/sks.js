/**
 * @return {Function}
 */
var createHelloWorld = function () {
  return function (...args) {
    return "Hello World";
  };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

// Runtime 56ms Beats 62.14%
// Memory 42.2MB Beats 9.31%
