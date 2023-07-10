function decode(encoded: number[], first: number): number[] {
  const answer = [first];

  while (encoded.length) {
    const num = encoded.shift();
    answer.push(num ^ answer[answer.length - 1]);
  }

  return answer;
}

// Runtime 118ms Beats 6.82%
// Memory 50MB Beats 15.91%
