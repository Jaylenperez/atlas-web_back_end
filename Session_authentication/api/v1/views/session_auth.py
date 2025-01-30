#!/usr/bin/env python3

"""Module for session authentication
"""
from flask import Response, request, jsonify, abort, make_response
from api.v1.views import app_views
from models.user import User
import os

@app_views.route('/auth_session/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login for session authentication
    Handles GET and POST requests to create a session for the user
    """
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check if email and password are provided
        if not email:
            return jsonify({"error": "email missing"}), 400
        if not password:
            return jsonify({"error": "password missing"}), 400

        # Retrieve user based on email
        user = User.search(email)
        if not user:
            return jsonify({"error": "no user found for this email"}), 404

        # Validate password
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        # Create session ID
        from api.v1.app import auth  # Import inside the function to avoid circular imports
        session_id = auth.create_session(user.id)

        # Create response and set cookie
        response = make_response(user.to_json())
        response.set_cookie(os.getenv("SESSION_NAME"), session_id)
        
        return response
    
    # Handle GET method: return a message indicating it's a method mismatch for GET
    return jsonify({"error": "Method Not Allowed"}), 405
