#!/usr/bin/env python3
"""insert"""


def insert_school(mongo_collection, **kwargs):
    """insert dict and return new id"""
    new_dict = kwargs
    inserting = mongo_collection.insert_one(new_dict)
    new_id = inserting.inserted_id
    return (new_id)
