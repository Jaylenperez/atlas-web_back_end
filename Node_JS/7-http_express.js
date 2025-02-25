const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 3000;

// Function to read the database asynchronously
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    
    const students = {};
    let totalStudents = 0;

    for (let i = 1; i < lines.length; i++) {
      const [firstname, , , field] = lines[i].split(',');
      if (firstname && field) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        totalStudents++;
      }
    }

    let response = `Number of students: ${totalStudents}`;
    for (const [field, names] of Object.entries(students)) {
      response += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
    }

    return response;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Route for the root path
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for /students
app.get('/students', async (req, res) => {
  const databasePath = process.argv[2]; // Get the database file from command-line arguments
  if (!databasePath) {
    res.status(500).send('Database file not provided');
    return;
  }

  let response = 'This is the list of our students\n';
  try {
    response += await countStudents(databasePath);
    res.send(response);
  } catch (error) {
    res.status(500).send('Cannot load the database');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Export the app variable
module.exports = app;
