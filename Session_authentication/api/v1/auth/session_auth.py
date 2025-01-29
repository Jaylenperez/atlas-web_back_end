#!/usr/bin/env python3
""" Module for Session Authentication class
"""
import uuid
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    """ Session Authentication class
    Manages session-based authentication.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates Session ID for a user_id.

        Args:
            user_id (str): The user ID to associate with the session.
        
        Returns:
            str: The generated session ID, or None if invalid.
        """

        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.__class__.user_id_by_session_id[session_id] = user_id

        return session_id


    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        
        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The associated user ID, or None if not found.
        """
        
        if session_id is None or not isinstance(session_id, str):
            return None
        
        return self.__class__.user_id_by_session_id.get(session_id)
    