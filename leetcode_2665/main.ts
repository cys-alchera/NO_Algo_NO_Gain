// Runtime 81ms [12.1%]
// Memory 45.6 MB

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

