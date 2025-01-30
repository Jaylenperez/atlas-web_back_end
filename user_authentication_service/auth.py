#!/usr/bin/env python3
"""
Authentication module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()  # Generate a salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash password
