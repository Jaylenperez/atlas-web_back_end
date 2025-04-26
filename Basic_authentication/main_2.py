#!/usr/bin/env python3
"""
Main script for testing BasicAuth.extract_base64_authorization_header.

This file runs a series of test cases to ensure that:
  - Invalid header values (None, non-string, missing prefix) return None.
  - Headers with the "Basic " prefix correctly return the Base64 credential portion.
"""

from api.v1.auth.basic_auth import BasicAuth  # Import the BasicAuth class

# Instantiate the BasicAuth helper
a = BasicAuth()

# 1) No header provided (None) should return None
print(a.extract_base64_authorization_header(None))  # -> None

# 2) Non-string input (e.g., integer) should return None
print(a.extract_base64_authorization_header(89))  # -> None

# 3) String without the "Basic " prefix should return None
print(a.extract_base64_authorization_header("Holberton School"))  # -> None

# 4) "Basic " prefix present but credential part not Base64 – 
#    method still extracts the part after the space without validating it
print(a.extract_base64_authorization_header("Basic Holberton"))  # -> "Holberton"

# 5) Well-formed Basic header: returns Base64 token (e.g., "SG9sYmVydG9u")
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))  # -> "SG9sYmVydG9u"

# 6) Header with padded Base64 string returns that full string intact
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
# -> "SG9sYmVydG9uIFNjaG9vbA=="

# 7) Missing space after "Basic" (e.g., "Basic1234") does not match pattern
#    and therefore returns None
print(a.extract_base64_authorization_header("Basic1234"))  # -> None
