#!/usr/bin/env python3
"""
Utility functions for filtering log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates values of specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace sensitive data with.
        message (str): Log message containing key-value pairs.
        separator (str): Separator between fields in the log.

    Returns:
        str: Obfuscated log message.
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
