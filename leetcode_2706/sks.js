/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function (prices, money) {
  const twoCheapestPrices = prices.sort((a, b) => a - b).slice(0, 2);
  const sum = twoCheapestPrices[0] + twoCheapestPrices[1];
  if (sum > money) {
    return money;
  }
  return money - sum;
};

// Runtime 96ms Beats 77.69%
// Memory 47.1MB Beats 27.31%
