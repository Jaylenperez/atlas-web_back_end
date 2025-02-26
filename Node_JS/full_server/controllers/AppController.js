// full_server/controllers/AppController.js

class AppController {
    // Static method to handle requests to the homepage
    static getHomepage(req, res) {
        // Set the response status to 200 and send the message
        res.status(200).send('Hello Holberton School!');
    }
}

// Export the AppController class for use in other files
export default AppController;
