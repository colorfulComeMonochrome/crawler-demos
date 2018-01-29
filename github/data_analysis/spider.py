from selenium import webdriver
import signal
import time

# 首先解析每一页的主播uri
def parse_page():

    for i in range(106):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        element = driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')
        print(element[5].text)
        try:
            print('start try!')
            with open('douyu.csv', 'a', encoding='utf-8')as f:
                print('open success')
                for i in element:
                    a = i.text.replace('\n', ',')
                    print(a)
                    f.write(a)
                    f.write('\n')
                    print('write success')
        except Exception as e:
            print(e)
            driver.close()
            driver.quit()
        # # 接受ctrl + c信号退出程序
        # driver.service.process.send_signal(signal.SIGTERM)
        next_page = driver.find_element_by_xpath('//*[@class="shark-pager-next"]')
        next_page.click()
        time.sleep(2)
        print('下一轮')


if __name__ == '__main__':
    # 启动selenium
    driver = webdriver.PhantomJS()
    driver.get('https://www.douyu.com/directory/all')
    print(driver.title)
    parse_page()
    driver.close()
    driver.quit()






