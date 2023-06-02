class SubrectangleQueries {
    box: number[][]

    constructor(rectangle: number[][]) {
        this.box = rectangle
    }

    updateSubrectangle(row1: number, col1: number, row2: number, col2: number, newValue: number): void {
        for (let rowIdx = row1; rowIdx <= row2; rowIdx++) {
            for (let colIdx = col1; colIdx <= col2; colIdx++) {
                this.box[rowIdx][colIdx] = newValue
            }
        }
    }

    getValue(row: number, col: number): number {
        return this.box[row][col]
    }
}

// Runtime 86 ms Beats 70.83%
// Memory 49.8 MB Beats 37.50%

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */