#!/usr/bin/env python3
"""
Main script for testing Base64 encoding of BasicAuth credentials.

This file:
  - Creates a User with a predefined email and password.
  - Prints the new user's ID and display name.
  - Generates the Base64-encoded credentials string suitable
    for use in an HTTP Basic Authorization header.
"""

import base64
from api.v1.auth.basic_auth import BasicAuth  # Imported for potential future use
from models.user import User

# ---------------------------------------------------------------------------
# STEP 1: Create and persist a test user with known credentials
# ---------------------------------------------------------------------------
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"

# Instantiate a new User object and set its email and clear-text password.
# The password setter will handle hashing under the hood.
user = User()
user.email = user_email
user.password = user_clear_pwd

# Display the new user's unique ID and full name (via display_name method)
print("New user: {} / {}".format(user.id, user.display_name()))

# Save the user record to the storage backend (e.g., file storage or database)
user.save()

# ---------------------------------------------------------------------------
# STEP 2: Prepare and print the Base64-encoded credentials
# ---------------------------------------------------------------------------
# 1) Concatenate email and password with a colon separator
basic_clear = "{}:{}".format(user_email, user_clear_pwd)

# 2) Convert the concatenated string to bytes using UTF-8 encoding
# 3) Encode those bytes to Base64
# 4) Decode the Base64 bytes back into a UTF-8 string
basic64 = base64.b64encode(basic_clear.encode('utf-8')).decode('utf-8')

# Output the Base64-encoded credentials string, ready for an
# Authorization header of the form: "Authorization: Basic <token>"
print("Basic Base64: {}".format(basic64))
