#!/usr/bin/env python3
"""
Main script for testing BasicAuth.extract_user_credentials.

This file runs a series of test cases to verify that:
  - Non-string or missing inputs return None.
  - Strings without the ":" separator return None.
  - Properly formatted credentials ("user:pass") return a (username, password) tuple.
"""

from api.v1.auth.basic_auth import BasicAuth  # Import the BasicAuth helper

# Instantiate the BasicAuth helper
a = BasicAuth()

# 1) None input should return None (invalid credentials)
print(a.extract_user_credentials(None))  # -> None

# 2) Non-string input (e.g., integer) should return None
print(a.extract_user_credentials(89))  # -> None

# 3) String missing the ":" separator is invalid; should return None
print(a.extract_user_credentials("Holberton School"))  # -> None

# 4) Properly formatted credentials "username:password" should return a tuple
print(a.extract_user_credentials("Holberton:School"))  # -> ("Holberton", "School")

# 5) Email-style username is supported; returns (username, password)
print(a.extract_user_credentials("bob@gmail.com:toto1234"))  # -> ("bob@gmail.com", "toto1234")
