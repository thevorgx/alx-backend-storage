#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

def vorg_tests():
    """Run test cases for the Cache class."""
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
    print("All vorg tests passed")

def main():
    """Main function to run the cache example and tests."""
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(f"Stored key: {key}")

    local_redis = redis.Redis()
    print(f"Data from Redis: {local_redis.get(key)}")

    vorg_tests()

if __name__ == "__main__":
    main()
