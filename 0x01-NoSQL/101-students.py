#!/usr/bin/env python3
"""for future Vorg:
the aggregation is on 2 steps:
1- using $project to assemble name and create a new temporary field named
averageScore where scores of each topic are added and averaged using $avg.
2- sort the average score using $sort, -1 means from top to bottom
ps: even the id is needed on the output didn't include it on the stage 1
because in Mongodb it's included by default."""


def top_students(mongo_collection):
    """return students with their avg score(descending order)"""
    aggregation_stages = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    top_studs = list(mongo_collection.aggregate(aggregation_stages))

    return (top_studs)
