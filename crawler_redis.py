# coding:'utf-8'
import threading
import time
import requests
import lxml.etree
import redis
import sys
import signal
from functools import partial

THREAD_NUMS = 10
DOWNLOAD_DELAY = 0.3
thread_on = True
threads = []
downloaded_pages = 0
r = redis.Redis()
start_url = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'


def fetch(url, raise_err=True):
    global downloaded_pages
    try:
        r = requests.get(url)
        downloaded_pages += 1
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)
    else:
        if raise_err:
            r.raise_for_status()
    finally:
        print('<%s> %s' % (r.status_code, url))


def parse(html):
    links = html.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href')
    for link in links:
        r.sadd('qianmu.seen', link)
        r.lpush('qianmu.queue', link)


def parse_university(html):
    container = lxml.etree.HTML(html)
    title = container.xpath('//*[@id="wikiContent"]/h1/text()')[0]
    infobox = container.xpath('//div[@class="infobox"]')[0]
    keys = infobox.xpath('./table/tbody/tr/td[1]/p/text()')
    cols = infobox.xpath('./table//tr/td[2]')
    values = [''.join(col.xpath('.//text()')) for col in cols]
    info = {title: dict(zip(keys, values))}
    r.lpush('qianmu.items', info)


def downloader(thread_name):
    while thread_on:
        link = r.lpop('qianmu.queue')
        try:
            parse_university(fetch(link, raise_err=False))
            print('剩余任务数:%s' % r.llen('qianmu.queue'))
        except Exception as e:
            print(e)
            print('网址打开失败')

        time.sleep(DOWNLOAD_DELAY)
    print('Thread-%s exited' % thread_name)


def signal_handler(signum, frame):
    print('received CTRL + C, wait for exit gracefully')
    global thread_on
    thread_on = False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        origin_url = sys.argv[1]
        dom = lxml.etree.HTML(fetch(origin_url))
        parse(dom)
    start_time = time.time()
    for i in range(THREAD_NUMS):
        t = threading.Thread(target=partial(downloader, i+1))
        t.start()
        threads.append(t)
        print('Thread-(%s) started' % i)

    signal.signal(signal.SIGINT, signal_handler)

    for t in threads:
        t.join()

    end_time = time.time()
    print('任务用时: %.3f, 下载页面:%s' % (end_time - start_time, downloaded_pages))
