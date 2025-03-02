const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('calculateNumber test ADD', function () {
    it('should return 6 when inputs are (1.4, 4.5)', function() {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
});

describe('calculateNumber test SUBTRACT', function () {
    it('should return -4 when inputs are (1.4, 4.5)', function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
});

describe('calculateNumber test DIVIDE', function () {
    it('should return 0.2 when inputs are (1.4, 4.5)', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
});

describe('calculateNumber test DIVIDE', function () {
    it('should return Error when inputs are (1.4, 0)', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error')
    });
});

describe('calculateNumber test DIVIDE', function () {
    it('should return Error when inputs are (0, 0)', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error')
    });
});