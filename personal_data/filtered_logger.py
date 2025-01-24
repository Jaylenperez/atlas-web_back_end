#!/usr/bin/env python3
"""
Module for filtering log messages,
custom log formatting, and database connection.
"""

import logging
import os
import mysql.connector
from typing import List
from utils import filter_datum

# Define the fields considered as Personally Identifiable Information (PII)
PII_FIELDS = (
    "name", "email", "phone", "ssn", "password"
)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the MySQL database using environment
    variables for credentials.

    Returns:
        mysql.connector.connection.MySQLConnection: Database
        connection object.
    """
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Check if db_name is set, since it is required
    if not db_name:
        raise ValueError("Database name (PERSONAL_DATA_DB_NAME) must be set.")

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to obfuscate.

        Args:
            fields (List[str]): List of fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Obfuscates sensitive fields in the log record's message.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with obfuscated sensitive fields.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for filtering user data logs.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler and set RedactingFormatter as its formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger
