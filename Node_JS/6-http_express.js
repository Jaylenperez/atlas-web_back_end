const express = require('express');

const app = express();
const port = 1245;

// Define the root route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Export the app variable
module.exports = app;
