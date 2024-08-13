#!/usr/bin/python
"""pymongo
"""
def update_topics(mongo_collection, name, topics):
    """changes all topics in a document based on name
    """
    mongo.collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )

