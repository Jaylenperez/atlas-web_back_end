// full_server/routes/index.js
import express from 'express';
import AppController from '../controllers/AppController'; // Import the AppController
import StudentsController from '../controllers/StudentsController'; // Import the StudentsController

const router = express.Router(); // Create an Express router

// Link the route / to the AppController
router.get('/', AppController.getHomepage);

// Link the route /students to the getAllStudents method
router.get('/students', StudentsController.getAllStudents);

// Link the route /students/:major to the getAllStudentsByMajor method
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router; // Export the router
