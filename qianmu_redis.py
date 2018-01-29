
from datetime import datetime, timedelta
import time
import random
import redis
import faker
r = redis.Redis()
f = faker.Faker('zh_CN')
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course, students=50):
    print('%s exam started' % course)
    for i in range(students):
        name = f.name()
        time_remaining = (DEADLINE - datetime.now()).total_seconds()
        score = '%s.%s' % (random.randint(60, 100), str(time_remaining).replace('.', ''))
        r.zadd(course, name, score)
        print('%s  %s' % (name, score))
        time.sleep(0.1)
    print('-' * 10 + '考试结束' + '-' * 10)


def top(course, rank_range=10):
    start, end = 0, rank_range - 1
    stus = r.zrevrange(course, start, rank_range, withscores=True)
    for i, (name, score) in enumerate(stus):
        print('%s:%s %s' % (i + 1, name.decode('utf-8'), score))
    print('-' * 30)


if __name__ == '__main__':
    courses = ['English', 'Math', 'Chinese']
    for course in courses:
        exam(course)
        top(course)


















