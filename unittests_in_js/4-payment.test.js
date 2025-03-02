const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', function () {
  let stub, consoleSpy;

  beforeEach(() => {
    // Stub Utils.calculateNumber to always return 10
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy on console.log
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and spy after each test
    stub.restore();
    consoleSpy.restore();
  });

  it('should stub calculateNumber and log correct message', function () {
    sendPaymentRequestToApi(100, 20);

    // Verify stub is called with exact arguments
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    // Verify console.log output
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
