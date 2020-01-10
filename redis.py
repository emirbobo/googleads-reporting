import redis

REDIS_HOST = '192.168.99.100'
REDIS_PORT = 6379

conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
