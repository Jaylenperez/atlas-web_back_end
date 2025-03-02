const { expect } = require('chai');
const request = require('request');

describe('Tests index', function() {
  // Checks for the right status code
  it('returns the correct status code: 200', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  // Checks for the right console.log output
  it('returns the correct console.log output', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Tests Cart Page', function() {
  // Checks for the right status code
  it('returns the correct status code: 200 if id is a number', function(done) {
    request('http://localhost:7865/cart/42', function(error, response, body) {
      // Status Code
      expect(response.statusCode).to.equal(200);
      
      // Console.log message
      expect(body).to.equal('Payment methods for cart 42');
      done();
    });
  });

  // Checks for the right console.log output
  it('returns 404 if id is not a number', function(done) {
    request('http://localhost:7865/cart/atlas', function(error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Tests payments page', function() {
  it('should return 200 status and an object', function(done) {
    request.get('http://localhost:7865/available_payments', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('Tests login page', function() {
  it('should display a welcome greeting', function(done) {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ userName: 'Michael' })
    };
    
    request(options, function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Michael');
      done();
    });
  });
});