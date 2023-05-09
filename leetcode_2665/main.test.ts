import { createCounter } from './main';
test('test case 1', () => {
    const counter = createCounter(5);
    expect(counter.increment()).toBe(6);
    expect(counter.reset()).toBe(5);
    expect(counter.decrement()).toBe(4);
});

test('test case 2', () => {
    const counter = createCounter(0);
    expect(counter.increment()).toBe(1); //
    expect(counter.increment()).toBe(2); //
    expect(counter.decrement()).toBe(1); //
    expect(counter.reset()).toBe(0); //
    expect(counter.reset()).toBe(0); //
});