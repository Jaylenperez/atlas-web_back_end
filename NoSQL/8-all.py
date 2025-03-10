#!/usr/bin/env python3
""""
This script lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    return mongo_collection.find()