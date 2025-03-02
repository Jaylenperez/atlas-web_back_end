const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with spy', function () {
  let consoleSpy;

  beforeEach(() => {
    // Spy on console.log before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the spy after each test
    consoleSpy.restore();
  });

  it('should log "The total is: 120" and be called once', function () {
    sendPaymentRequestToApi(100, 20);

    // Verify console.log output
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" and be called once', function () {
    sendPaymentRequestToApi(10, 10);

    // Verify console.log output
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;

    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
