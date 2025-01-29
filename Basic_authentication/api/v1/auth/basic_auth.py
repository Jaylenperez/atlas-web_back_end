#!/usr/bin/env python3
"""
Basic authentication class
"""
import base64
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


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 part of the Authorization header.

        Arguments:
            base64_authorization_header (str): The Base64 encoded string

        Returns:
            str: The decoded value as a UTF-8 string, or None if invalid
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
