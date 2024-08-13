#usr/bin/python
"""Module : pymongo
"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a new doc to collection based on kwargs
    """
    db = mongo_collection.insert_one(kwargs)
    return db.inserted_id

