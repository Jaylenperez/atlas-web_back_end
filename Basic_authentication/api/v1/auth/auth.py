#!/usr/bin/env python3
"""
Auth module for API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required
        Arguments:
            path: string representing the requested path
            excluded_paths: list of paths that do not require authentication
        Return:
            False (default, for now)
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from a request object
        Arguments:
            request: Flask request object
        Return:
            None (default, for now)
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user
        Arguments:
            request: Flask request object
        Return:
            None (default, for now)
        """
        return None
