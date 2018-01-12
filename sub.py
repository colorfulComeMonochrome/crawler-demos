
import redis


config = {
    'host': '10.0.104.66',
    'port': 6379,
    'db': 0
}
r = redis.Redis(**config)
channels = ['1707', '1706', 'world']


if __name__ == '__main__':
    pubsub = r.pubsub()
    for channel in channels:
        pubsub.subscribe(channel)

    while True:
        for item in pubsub.listen():
            msg = item['data']
            if isinstance(msg, int):
                print('listen to %s succ' % item['channel'])
                continue
            print('%s:%s' % (item['channel'], msg.decode('utf-8')))














