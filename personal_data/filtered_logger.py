#!/usr/bin/env python3
"""
Module for filtering log messages and custom log formatting.
"""

import logging
from typing import List
from utils import filter_datum


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
