// full_server/controllers/StudentsController.js
import readDatabase from '../utils'; // Import the readDatabase function

class StudentsController {
    // Static method to get all students
    static async getAllStudents(req, res) {
        try {
            const students = await readDatabase('./database.csv'); // Read the database file
            res.status(200).send('This is the list of our students\n' + // Send the initial message
                Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase())) // Sort fields alphabetically
                    .map((field) => {
                        return `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`; // Format the output
                    })
                    .join('\n') // Join each field's information with a newline
            );
        } catch (error) {
            // Handle error if the database cannot be loaded
            res.status(500).send('Cannot load the database');
        }
    }

    // Static method to get students by major
    static async getAllStudentsByMajor(req, res) {
        const { major } = req.params; // Get the major parameter from the request

        // Validate the major parameter
        if (major !== 'CS' && major !== 'SWE') {
            return res.status(500).send('Major parameter must be CS or SWE'); // Respond with an error if invalid
        }

        try {
            const students = await readDatabase('./database.csv'); // Read the database file
            res.status(200).send(`List: ${students[major].join(', ')}`); // Send the list of first names for the specified major
        } catch (error) {
            // Handle error if the database cannot be loaded
            res.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController; // Export the StudentsController class
