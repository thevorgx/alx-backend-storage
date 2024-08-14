#!/usr/bin/env python3
""" Main file """
def main():
    Cache = __import__('exercise').Cache


    cache = Cache()

    data1 = b"foo"
    data2 = b"bar"
    data3 = 42
    key1 = cache.store(data1)
    key2 = cache.store(data2)
    key3 = cache.store(data3)
    
    print(f"Stored keys: {key1}, {key2}, {key3}")

    local_redis = redis.Redis()
    print(f"Data from Redis: {local_redis.get(key1)}, {local_redis.get(key2)}, {local_redis.get(key3)}")

    replay(cache.store)

if __name__ == "__main__":
    main()