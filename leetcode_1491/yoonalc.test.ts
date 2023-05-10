import { average } from './yoonalc';
test('test case 1', () => {
    const res = average([4000, 3000, 1000, 2000]);
    expect(res).toBe(2500.00000);
});

test('test case 2', () => {
    const res = average([1000, 2000, 3000]);
    expect(res).toBe(2000.00000); //
});

test('test case 3', () => {
    const res = average([8000,9000,2000,3000,6000,1000]);
    expect(res).toBe(4750.00000); //
});