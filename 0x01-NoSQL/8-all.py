#!/usr/bin/env python3
"""Mongo db
"""

def list_all(mongo_collection):
    """List all documents in a mongo collection
    """
    return [doc for doc in mongo_collection.find()]
