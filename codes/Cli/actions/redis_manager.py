#

import redis

class RedisManager:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def get_redis_connection(self):
        return self.r
