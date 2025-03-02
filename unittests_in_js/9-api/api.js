const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const { id } = req.params;
  const regex = /^\d+$/;
  if (!regex.test(id)) {
    res.status(404).send('Invalid ID format');
    return;
  }
  res.send(`Payment methods for cart ${id}`)
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865')
});

module.exports = app;