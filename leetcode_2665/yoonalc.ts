// Runtime 81ms Beats 12.01%
// Memory 45.6MB Beats 42.76%

type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

export function createCounter(init: number): ReturnObj {
    let count = init
    return {
        increment: () => count+=1,
        decrement: () => count-=1,
        reset: () => count=init,
    }
};

