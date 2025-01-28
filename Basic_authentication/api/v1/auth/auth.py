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
        Determines if a path requires authentication
        Args:
            path (str): The path to check
            excluded_paths (List[str]): List of paths that don't require authentication
        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # Ensure path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

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
