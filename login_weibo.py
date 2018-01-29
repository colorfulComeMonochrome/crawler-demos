import time
import requests
from selenium import webdriver




def login(username):
    driver = webdriver.Chrome()
    driver.get('https://weibo.com')
    # print(os.listdir('/home/rock/crawler'))
    with open('/home/rock/crawler/weibo.txt')as f:
        passwd = f.read()
    time.sleep(5)
    input_username = driver.find_element_by_id('loginname')
    for i in username:
        input_username.send_keys(i)
        time.sleep(0.1)
    input_passwd = driver.find_element_by_xpath("//input[@type='password']")
    for j in passwd:
        input_passwd.send_keys(j)
        time.sleep(0.1)
    time.sleep(1)
    btn = driver.find_element_by_xpath('//a[@action-type="btn_submit"][1]')
    time.sleep(10)
    btn.click()
    time.sleep(1)
    cookies = driver.get_cookies()
    username = driver.find_element_by_xpath('//a[@class="name S_txt1"]').text
    print(username)
    request_cookies = {cookie['name']: cookie['value'] for cookie in cookies}

    print(request_cookies)
    response = requests.get('https://weibo.com', headers=request_cookies,)
    response.text.find('username')

    # 翻到页面底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    feeds = driver.find_elements_by_xpath('//div[@node-type="feed_list_content"]')
    print(type(feeds))
    print(feeds)
    for feed in feeds:
        print(feed.text)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    username = '13664069165'
    login(username)













