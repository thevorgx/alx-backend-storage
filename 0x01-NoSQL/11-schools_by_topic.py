#!/usr/bin/env python3
"""schools by a topic"""


def schools_by_topic(mongo_collection, topic):
    """return a list of schools by a topic"""
    by_topic = {"topics": topic}
    schools_list = list(mongo_collection.find(by_topic))
    return (schools_list)
