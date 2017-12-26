# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree

import time

def load_data_setting():

    # 1.创建 session
    session = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.https://www.zhihu.com/ 获取 xsrf
    xsrf_url = "https://www.zhihu.com/"
    xsrf_data = session.get(xsrf_url, headers=headers, verify=False).content
    xsrf = analysis_data(xsrf_data)

    # 2.发送验证码 获取验证码的参数:保存图片
    # https://www.zhihu.com/captcha.gif?r=1513858445316&type=login&lang=cn
    # https://www.zhihu.com/captcha.gif?&type=login&lang=cn&r= + "时间"
    captch_url = "https://www.zhihu.com/captcha.gif?&type=login&lang=en&r=" + str(int(time.time()*1000))
    captch_data = session.get(captch_url, headers=headers, verify=False).content
    write_file(captch_data)
    captch_code = raw_input("请输入验证码:")

    # 3.发送登录 -->cookie
    login_url = "https://www.zhihu.com/login/phone_num"
    formdata = {
        "phone_num": "xxxxxx",
        "password": "xxxxxx",
        "_xsrf": xsrf,
        "captcha": captch_code,
        "captcha_type": "en"
    }
    session.post(login_url, data=formdata, headers=headers)

    # 4.发送 设置的网址的数据https://www.zhihu.com/settings/profile
    setting_url = "https://www.zhihu.com/settings/profile"
    data = session.get(setting_url, headers=headers).content

    print data

def analysis_data(data):
    soup = BeautifulSoup(data, "lxml")
    xsrf = soup.select("input[name='_xsrf']")[0].get("value")
    return xsrf


def write_file(data):
    with open("7code.png", "wb") as f:
        f.write(data)

if __name__ == '__main__':
    load_data_setting()







