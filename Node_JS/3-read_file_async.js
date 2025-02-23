const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Read the database file asynchronously
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');

    // Get the number of students
    const numberOfStudents = lines.length - 1; // Subtracting the header
    console.log(`Number of students: ${numberOfStudents}`);

    const fieldCounts = {};
    
    // Process each line, skipping the header
    lines.slice(1).forEach((line) => {
      const [firstname, lastname, age, field] = line.split(',');
      if (field) {
        if (!fieldCounts[field]) {
          fieldCounts[field] = [];
        }
        fieldCounts[field].push(firstname);
      }
    });

    // Log student counts per field
    for (const [field, names] of Object.entries(fieldCounts)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

    return Promise.resolve();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
