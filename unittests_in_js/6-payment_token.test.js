const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
  it('should return a resolved promise with correct data when success is true', function (done) {
    getPaymentTokenFromAPI(true).then((response) => {
      expect(response).to.deep.equal({ data: 'Successful response from the API' });
      done(); // Ensure the test completes properly
    }).catch((err) => done(err)); // Handle unexpected errors
  });
});
