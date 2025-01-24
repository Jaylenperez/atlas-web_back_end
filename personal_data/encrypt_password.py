#!/usr/bin/env python3
"""
Module for password encryption and hashing using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and return the salted, hashed password.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.

    Example:
        >>> hash_password("MyAmazingPassw0rd")
        b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
    """
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')

    # Generate a salt with the default work factor (12 rounds)
    salt = bcrypt.gensalt(rounds=12)

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
