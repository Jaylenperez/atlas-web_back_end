#!/usr/bin/env python3
"""Find schools that have a specific topic in MongoDB"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents containing the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
