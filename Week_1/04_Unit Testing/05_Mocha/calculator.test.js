const assert = require('assert');
const { add, subtract } = require('./calculator');

describe('Calculator Tests', function () {

    it('should add two numbers', function () {
        assert.strictEqual(add(10, 5), 15);
    });

    it('should subtract two numbers', function () {
        assert.strictEqual(subtract(10, 5), 5);
    });

});