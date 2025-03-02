const express = require('express');
const app = express();

app.use(express.json());

// INDEX PAGE
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// CART PAGE
app.get('/cart/:id', (req, res) => {
  const { id } = req.params;
  const regex = /^\d+$/;
  if (!regex.test(id)) {
    res.status(404).send('Invalid ID format');
    return;
  }
  res.send(`Payment methods for cart ${id}`)
});

// PAYMENTS PAGE
app.get('/available_payments', (req, res) => {
  res.status(200).json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// LOGIN PAGE
app.post('/login', (req, res) => {
  const userName = req.body.userName;
  res.status(200).send(`Welcome ${userName}`)
});

// To be displayed when server is connected
app.listen(7865, () => {
  console.log('API available on localhost port 7865')
});

module.exports = app;