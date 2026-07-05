const { add, subtract } = require('./calculator');

test('adds two numbers', () => {
    expect(add(10, 5)).toBe(15);
});

test('subtracts two numbers', () => {
    expect(subtract(10, 5)).toBe(5);
});