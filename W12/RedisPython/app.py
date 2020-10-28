import redis

r = redis.StrictRedis(
    host='104.198.244.0',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

r.set('ip_address', '0.0.0.5')
r.set('last_visited', 'account', 86400)
r.set('idx', '1')

print("ip: ", r.get('ip_address'))

r.lpush('List1', 'A')
r.lpush('List2', 'B')
r.lpush('List3', 'C')

myredcord = {
    "name": "Hackers y Slackers",
    "description": "Mediocre tutorials",
    "website": "https://hackersandslackers.com/",
    "github": "https://gothub.com/hackersandslackers"
}

print("My hash : ", r.hgetall('myhash'))