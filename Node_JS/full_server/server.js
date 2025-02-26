// full_server/server.js
import express from 'express'; // Import Express
import router from './routes/index'; // Import the routes

const app = express(); // Create an instance of Express
const port = 1245; // Set the port to 1245

// Use the routes defined in the routes file
app.use(router);

// Start the server and listen on the defined port
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`); // Log the server URL
});

// Export the Express app for external usage (for testing, etc.)
export default app;
