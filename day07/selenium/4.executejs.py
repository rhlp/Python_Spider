# -*- coding:utf-8 -*-

from selenium import webdriver

def load_data():
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs',service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    driver.get("http://www.baidu.com")

    # 通过js 代码修改 搜索框的颜色
    js_code = "var ele = document.getElementById('kw');ele.style.border = '1px solid red'"

    # 修改
    driver.execute_script(js_code)

    # 快照
    driver.save_screenshot("4js.png")

if __name__ == '__main__':
    load_data()
