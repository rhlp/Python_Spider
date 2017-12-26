# -*- coding:utf-8 -*-

from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def selenium_base_use():

    # 1.创建浏览器对象
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs',service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

    # 2.请求数据
    driver.get("https://www.baidu.com")

    # 3.获取内容
    data = driver.page_source

    with open("1baidu.html", "w") as f:
        f.write(data)

    # 4.点击 新闻 按钮
    driver.find_element_by_name('tj_trnews').click()

    # 5.给输入框 输入数据 unicode 编码
    driver.find_element_by_id("ww").send_keys(u"圣诞节")

    # 6.点击 百度一下 按钮
    driver.find_element_by_class_name("btn").click()

    # 7.点击第一条的新闻
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

    # 8.找到新开的页面 打印结果为 list列表
    print driver.window_handles

    # 9.根据角标可以切换页面
    driver.switch_to.window(driver.window_handles[1])

    # 10.再次返回上一个页面
    driver._switch_to.window(driver.window_handles[0])

    # 11.当前的网址
    current_url = driver.current_url

    # 12.获取所有的cookie
    driver.get_cookies()

    # 13.关闭当前页面
    driver.close()
    # 关闭浏览器
    driver.quit()

    # 快照，必须以 png 结尾
    driver.save_screenshot("1baidu.png")

if __name__ == '__main__':
    selenium_base_use()


