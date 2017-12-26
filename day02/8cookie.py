# -*- coding:utf-8 -*-

import urllib2

def send_request():
    # 1.url --直接访问登录后的数据
    url = "http://www.renren.com/410043129/profile"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Cookie":"anonymid=jbbjvcqslf53au; depovince=GW; _r01_=1; JSESSIONID=abc47St_fad2b5KdSvNbw; ick_login=dcf753ad-06f6-4eea-9b6a-6a323342a04a; ick=02099ef1-519e-432d-9a17-fa2bd871e05a; __utma=151146938.1010603587.1513562321.1513562321.1513562321.1; __utmc=151146938; __utmz=151146938.1513562321.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=151146938.2.10.1513562321; jebecookies=0b3bae1c-4c99-44a6-9e8d-80379ed01eb2|||||; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=503e316f6c0b733552952070082140279; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20171217/2145/main_mJgh_b0450000a72e195a.jpg; t=6807c5f2b3401a7523b041a16682291e9; societyguester=6807c5f2b3401a7523b041a16682291e9; id=327550029; xnsid=989a5ddc; loginfrom=syshome; jebe_key=f7d40357-7f9f-4d11-9cc5-f25dca61c884%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1513563205145%7C1%7C1513563204316; wp_fold=0; ch_id=10050; BAIDU_SSP_lcr=https://www.baidu.com/link?url=kVW6EUl-6udomX4T4DFokOvnjs-VsRq6Lr7U7-hKuAC&wd=&eqid=e11537fc00003a57000000035a37270f; _ga=GA1.2.1010603587.1513562321; _gid=GA1.2.1935990284.1513563967"}

    # 3.request
    request = urllib2.Request(url, headers=headers)

    # 发送请求
    response = urllib2.urlopen(request)

    # 返回数据
    return response.read()

def write_file(data):
    with open("8renren.html", "w") as f:
        f.write(data)


if __name__ == '__main__':
    data = send_request()
    write_file(data)