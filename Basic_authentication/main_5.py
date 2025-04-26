#!/usr/bin/env python3
"""
Main script for testing BasicAuth.user_object_from_credentials.

This file demonstrates how to:
  - Create and persist a new User with randomized credentials.
  - Attempt to retrieve a User object using the BasicAuth helper under various scenarios.
  - Verify that only correct (email, password) combinations return a valid User.
"""

import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

# ---------------------------------------------------------------------------
# STEP 1: Create and save a new test User with random email and password
# ---------------------------------------------------------------------------

# Generate a unique email and password using UUIDs to avoid collisions
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())

# Instantiate a new User object and assign its fields
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd  # setter will handle hashing

# Display the created user's full name
print("New user: {}".format(user.display_name()))

# Persist the new user to storage (e.g., file, database)
user.save()

# ---------------------------------------------------------------------------
# STEP 2: Test BasicAuth.user_object_from_credentials with various inputs
# ---------------------------------------------------------------------------

# Instantiate the BasicAuth helper
auth = BasicAuth()

# 1) No credentials provided (None, None) → should return None
u = auth.user_object_from_credentials(None, None)
print(u.display_name() if u else "None")

# 2) Invalid types for credentials (int, int) → should return None
u = auth.user_object_from_credentials(89, 98)
print(u.display_name() if u else "None")

# 3) Non-existent email with arbitrary password → should return None
u = auth.user_object_from_credentials("email@notfound.com", "pwd")
print(u.display_name() if u else "None")

# 4) Correct email but wrong password → should return None
u = auth.user_object_from_credentials(user_email, "pwd")
print(u.display_name() if u else "None")

# 5) Correct email and correct password → should return the User object
u = auth.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u else "None")
