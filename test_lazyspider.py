from lazyspider.lazyspider import LazyHeaders


curl = """curl 'https://www.baidu.com/' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Connection: keep-alive' --compressed"""

lh = LazyHeaders(curl)

headers = lh.getHeaders()
cookies = lh.getCookies()

print('Headers:{}'.format(headers))
print('*' * 40)
print(headers)
print('*' * 40)
print('Cookies:{}'.format(cookies))




