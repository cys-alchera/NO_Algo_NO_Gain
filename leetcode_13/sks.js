/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  const romanNumeralsMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  }

  let result = 0;
  let prevValue = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    const currentCharacter = s[i];
    const currentValue = romanNumeralsMap[currentCharacter];

    if (currentValue >= prevValue) {
      result += currentValue;
    } else {
      result -= currentValue;
    }
    prevValue = currentValue;
  }

  return result;
};

// Runtime 118ms Beats 88.65%
// Memory 47.2MB Beats 69.34%
