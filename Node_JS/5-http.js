const http = require('http');
const fs = require('fs');

// Function to count students from the CSV file
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      const numberOfStudents = lines.length - 1; // Subtracting the header
      const fieldCounts = {};

      // Process each line, skipping the header
      lines.slice(1).forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (field) {
          if (!fieldCounts[field]) {
            fieldCounts[field] = [];
          }
          fieldCounts[field].push(firstname);
        }
      });

      // Prepare the response message
      let responseMessage = `Number of students: ${numberOfStudents}\n`;
      for (const [field, names] of Object.entries(fieldCounts)) {
        responseMessage += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(responseMessage);
    });
  });
}

// Create an HTTP server
const app = http.createServer((req, res) => {
  const url = req.url;

  // Handle the root URL
  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!\n');
  } 
  // Handle the /students URL
  else if (url === '/students') {
    const databasePath = process.argv[2]; // Get the database file path from command line argument

    countStudents(databasePath)
      .then((studentsInfo) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\n${studentsInfo}`);
      })
      .catch((error) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(error.message);
      });
  } 
  // Handle other URLs
  else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found\n');
  }
});

// Make the server listen on port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

// Export the app variable
module.exports = app;
