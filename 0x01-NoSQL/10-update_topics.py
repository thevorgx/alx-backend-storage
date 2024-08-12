#!/usr/bin/env python3
"""update topics"""


def update_topics(mongo_collection, name, topics):
    """update school topics base on a filtering by name"""
    filt_er = {"name": name}
    new_topic = {"topics": topics}
    mongo_collection.update_many(filt_er, {"$set": new_topic})
