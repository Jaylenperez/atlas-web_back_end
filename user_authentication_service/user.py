#!/usr/bin/env python3
"""
User module for authentication service
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    SQL Alchemy model for 'users' class

    Attributes:
        id(int): Primary key.
        email (str): Unique email for the user (non-nullable)
        hashed_password (str): Hashed password of the user (non-nullable).
        session_id (str): Session identifier for authentication (nullable).
        reset_token (str): Token for password reset (nullable).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False, unique=True)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __repr__(self):
        return (
            "<User(email='{email}', hashed_password='{hashed_password}', "
            "session_id='{session_id}', reset_token='{reset_token}')>".format(
                email=self.email,
                hashed_password=self.hashed_password,
                session_id=self.session_id,
                reset_token=self.reset_token
            )
        )
