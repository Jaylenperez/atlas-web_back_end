#!/usr/bin/env python3
"""
Basic authentication class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication class inheriting from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part from the Authorization header for Basic Authentication

        Arguments:
            authorization_header (str): The Authorization header from the request

        Returns:
            str: The Base64 part of the Authorization header or None
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
