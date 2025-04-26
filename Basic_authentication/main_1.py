#!/usr/bin/env python3
"""
Main script for testing the Auth.require_auth method.

This file executes a series of test cases to confirm that:
  - Missing paths or exclusion lists default to requiring authentication.
  - Specific endpoints listed in the exclusion list do not require authentication.
  - Partial or mismatched paths are handled correctly.
"""

from api.v1.auth.auth import Auth  # Import the Auth class from our authentication module

# Create an Auth instance to test its require_auth behavior
a = Auth()

# 1) No path provided and no exclusions: should require authentication by default.
#    expect True
print(a.require_auth(None, None))

# 2) No path provided but an empty exclusion list: still requires authentication.
#    expect True
print(a.require_auth(None, []))

# 3) Path provided but no exclusions: should require authentication.
#    expect True
print(a.require_auth("/api/v1/status/", []))

# 4) Path matches an entry in the exclusion list (with trailing slash):
#    should not require authentication.
#    expect False
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))

# 5) Path without trailing slash does not exactly match the excluded path:
#    still treated as requiring authentication because the pattern must match exactly.
#    expect False
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))

# 6) Different endpoint than those in exclusions: requires authentication.
#    expect True
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))

# 7) Exclusion list contains unrelated endpoints: users endpoint still requires auth.
#    expect True
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
