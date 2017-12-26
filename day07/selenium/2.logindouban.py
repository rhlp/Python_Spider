# -*- coding:utf-8 -*-

from selenium import webdriver

def login_douban():

    # 1.创建浏览器对象
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs',service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

    # 2.发送请求
    driver.get("https://www.douban.com/accounts/login?source=movie")
    driver.save_screenshot("2doubancode.png")
    code = raw_input("请输入验证码:")

    # 3.填充 用户名 密码 验证码
    driver.find_element_by_name('form_email').send_keys(u'mr.mao.tony@gmail.com')
    driver.find_element_by_name('form_password').send_keys(u'ALARMCHIME')
    driver.find_element_by_id('captcha_field').send_keys(code)

    # 4.点击登陆
    driver.find_element_by_name('btn-submit').click()

    # 5.是否发送成功
    driver.save_screenshot("2logined.png")

if __name__ == '__main__':
    login_douban()


    # zip 函数的应用

    # list_one = [1, 2, 3]
    # list_two = ["a", "b", "c"]
    # list_three = [100, 200, 300]
    #
    # all_list = zip(list_one, list_two, list_three)
    #
    # for one, two, thre in all_list:
    #     print one
    #     print two
    #     print thre

