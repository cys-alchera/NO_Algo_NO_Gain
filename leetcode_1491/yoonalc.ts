// Runtime 60 ms, Beats 62.85%
// Memory 44.1 MB, Beats 5.25%

export function average(salary: number[]): number {
    const v = salary.reduce(
        (acc, cur) => {
            return [
                Math.min(cur, acc[0]),
                Math.max(cur, acc[1]),
                acc[2] + cur,
            ]
        }, [Infinity, -Infinity, 0]
    );

    return (v[2] - (v[0]+v[1])) / (salary.length - 2)
};