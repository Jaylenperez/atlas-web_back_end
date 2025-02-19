#!/usr/bin/env python3
"""
Insert a document into a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: key-value pairs to insert as the document.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
