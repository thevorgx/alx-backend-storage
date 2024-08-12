#!/usr/bin/env python3
"""find docs"""


def list_all(mongo_collection):
    """find all documents in a collection"""
    doc_list = list(mongo_collection.find())
    return (doc_list)
