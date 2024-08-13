#!/usr/bin/python
"""Mongo db
"""

def list_all(mongo_collection):
    """List all documents in a mongo collection
    """
    return [doc for doc in mongo_collection.find()]
