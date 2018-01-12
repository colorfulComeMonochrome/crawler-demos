
import faker
import redis
import sys

config = {
    'host': '10.0.104.66',
    'port': 6379,
    'db': 0
}
r = redis.Redis(**config)
faker = faker.Faker('zh_CN')

if __name__ == '__main__':
    channel = sys.argv[1]
    while True:
        # name = faker.name()
        name = '华佗'
        # message = '12345,上山打老虎,老虎没打着,打到小凶许'
        message = input('Please input some message:\n')
        if message.lower() == 'exit':
            break
        information = '{name}: {message}'.format(**locals())
        r.publish(channel, information)




