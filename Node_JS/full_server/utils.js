import fs from 'fs/promises';

async function readDatabase(filePath) {
    // Return a new promise that will resolve with student data or reject with an error
    return new Promise(async (resolve, reject) => {
        try {
            // Read file asynchronously
            const data = await fs.readFile(filePath, 'utf8');

            // Trim extra whitespace, split data by new lines, and remove the first line (header row)
            const lines = data.trim().split('\n').slice(1);

            // Create empty object to store names grouped by field.
            const students = {};

            // Iterate over each line (representing a student record)
            lines.forEach((line) => {
                // Split the line by commas to extract student details.
                const [firstname, lastname, age, field] = line.split(',');

                // If the field category does not exist in the students object, initialize it as an empty array
                if (!students[field]) {
                    students[field] = [];
                }

                // Add students first name to the respective field category
                students[field].push(firstname);
            });

            // Resolve the Promise with the student object, containing categorized names.
            resolve(students);
        } catch (error) {
            // If theres an error, reject promise with a error message.
            reject(new Error('Cannot load the database'));
        }
    });
}

// Export the readDatabase function so it can be used for other files.
export default readDatabase;
