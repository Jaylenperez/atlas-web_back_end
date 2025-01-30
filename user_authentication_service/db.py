#!/usr/bin/env python3
"""
DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email.
            hashed_password (str): The hashed password.

        Returns:
            User: The created User object with an assigned id.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session  # Get the session
        session.add(new_user)  # Add the new user to the session
        session.commit()  # Commit to persist changes
        return new_user  # Return the created user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering.

        Returns:
            User: The first user that matches the criteria.

        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If the query arguments are invalid.
        """
        session = self._session  # Get the session

        # Ensure all provided keys are valid column names
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError(f"Invalid filter: {key}")

        # Query the database using filter_by
        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found with given criteria.")

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes in the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments representing
            fields to update.

        Raises:
            ValueError: If an invalid attribute is passed.
            NoResultFound: If the user is not found.
        """
        session = self._session  # Get the session
        user = self.find_user_by(id=user_id)  # Locate the user

        # Ensure all provided keys are valid column names
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise ValueError(f"Invalid attribute: {key}")

        # Update user attributes
        for key, value in kwargs.items():
            setattr(user, key, value)

        session.commit()  # Commit changes
