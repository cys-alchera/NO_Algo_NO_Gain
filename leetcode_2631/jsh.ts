declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function (fn) {
    const obj = {}
    for (let i = 0; i < this.length; i++) {
        const key = fn(this[i])
        if (obj[key]) obj[key].push(this[i])
        else obj[key] = [this[i]]
    }
    return obj
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

// Runtime 143 ms Beats 74.56%
// Memory 64.5 MB Beats 50.30%