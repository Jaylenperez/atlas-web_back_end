#!/usr/bin/env python3
"""
Main script for testing BasicAuth.decode_base64_authorization_header.

This file runs a series of test cases to verify that:
  - Non-string or malformed Base64 inputs return None.
  - Properly padded Base64 strings decode to their original form.
  - Integration with extract_base64_authorization_header works end-to-end.
"""

from api.v1.auth.basic_auth import BasicAuth  # Import the BasicAuth helper

# Instantiate the BasicAuth helper
a = BasicAuth()

# 1) None input should not decode and thus return None
print(a.decode_base64_authorization_header(None))  # -> None

# 2) Non-string input (e.g., integer) should return None
print(a.decode_base64_authorization_header(89))  # -> None

# 3) String that isn't Base64 (no padding or invalid chars) should return None
print(a.decode_base64_authorization_header("Holberton School"))  # -> None

# 4) Valid Base64 without padding; this specific string ("SG9sYmVydG9u") decodes to "Holberton"
print(a.decode_base64_authorization_header("SG9sYmVydG9u"))  # -> "Holberton"

# 5) Properly padded Base64 string decodes correctly, including spaces
#    ("SG9sYmVydG9uIFNjaG9vbA==" decodes to "Holberton School")
print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))  # -> "Holberton School"

# 6) End-to-end test: extract the Base64 token from a Basic header,
#    then decode it. Should yield "Holberton School".
token = a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")
print(a.decode_base64_authorization_header(token))  # -> "Holberton School"
