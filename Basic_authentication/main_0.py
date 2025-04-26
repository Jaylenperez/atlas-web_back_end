#!/usr/bin/env python3
"""
Main script for demonstrating the Auth class methods.
This file shows how to:
  - determine whether a request path requires authentication
  - fetch the HTTP Authorization header
  - identify the current user based on that header
"""

# Import the Auth class from our versioned API authentication module
from api.v1.auth.auth import Auth

# Create an Auth instance to use its methods below
a = Auth()

# 1) Check if the path "/api/v1/status/" requires authentication.
#    The second argument is a list of paths exempt from auth.
#    Returns True if authentication is required, False otherwise.
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))

# 2) Retrieve the Authorization header from the incoming request.
#    If no header is present, this will return None.
print(a.authorization_header())

# 3) Based on the Authorization header (e.g., a bearer token),
#    return the corresponding user object or None if not authenticated.
print(a.current_user())
