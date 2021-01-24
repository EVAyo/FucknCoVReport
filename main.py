# coding:utf-8
import requests
from http import cookiejar
from bs4 import BeautifulSoup
import time
# import iMessage
import base64
import datetime
import random
import esprima
import re


class STUPost:
    def __init__(self):
        self.uname = ''  # Your Student Number, e.g. 2001200001
        self.upwd = ''  # You ID card: last 6 numbers, e.g. 123456
        self.cookies = {}
        # mock the build-in browser of WeChat:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2575 MMWEBSDK/200701 Mobile '
                          'Safari/537.36 MMWEBID/4039 MicroMessenger/7.0.17.1720(0x27001137) Process/tools '
                          'WeChat/arm64 NetType/WIFI Language/en ABI/arm64',
            'Referer': 'http://stu.cugb.edu.cn/webApp/xuegong/index.html',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        # mock the others
        # self.headers ={'User-Agent': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}
        self.session = requests.session()
        self.message1 = ''
        self.message2 = ''
        self.subj = ''
        self.content = ''

    def login(self):
        try:
            url = 'https://cas.cugb.edu.cn/login'
            req = self.session.request('GET', url, verify=False).content
            soup = BeautifulSoup(req, 'html.parser')
            execution = soup.findAll("input", {"name": "execution"})[0]["value"]
            system = soup.findAll("input", {"id": "userLoginSystem"})[0]["value"]
            data = {'username': self.uname,
                    'password': self.upwd,
                    'execution': execution,
                    '_eventId': 'submit',
                    'geolocation': '',
                    'loginType': 'username',
                    'system': system,  # '27A5A4DF0C874122A0AFE0367F0A3F46'
                    'enableCaptcha': 'N'}
            req = self.session.post(url=url, data=data, headers=self.headers, verify=False)
            self.cookies = requests.utils.dict_from_cookiejar(req.cookies)
            time.sleep(3)
            # To get the uid from javascript:
            uidurl = 'https://stu.cugb.edu.cn/'
            req = self.session.request('GET', uidurl, cookies=self.cookies, headers=self.headers, verify=False).content
            soup = BeautifulSoup(req, 'html.parser')
            scriptTags = str(soup.findAll('script')[1])
            rexp = re.compile(r'<[^>]+>', re.S)
            scriptCode = rexp.sub('', scriptTags)
            uid = esprima.tokenize(scriptCode)[48].value.replace('\'', '')
            uiddata = {'uid': uid}
            req = self.session.request('POST', "https://stu.cugb.edu.cn:443/caswisedu/login.htm", data=uiddata,
                                       verify=False)
            time.sleep(3)
            content = self.session.post(
                'http://stu.cugb.edu.cn/webApp/xuegong/index.html#/zizhu/apply?projectId'
                '=4a4ce9d6725c1d4001725e38fbdb07cd&type=YQSJCJ',
                verify=False)
            if content.status_code == 200:
                self.message1 = "Login status: Succeeded"
                time.sleep(3)
                self.clock_in()
            else:
                self.message1 = "Login status: Failed"
        except Exception as e:
            self.message1 = 'Error Code 0: ' + str(e)

    def clock_in(self):
        # cookie_para = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        data = {
            'data': '''{"xmqkb":{"id":"4a4ce9d6725c1d4001725e38fbdb07cd"},"c1":"36.9℃以下","c2":"健康","c17":"否",
            "c4":"否","c5":"否","c6":"否","c9":"否","c7":"否","type":"YQSJCJ",
            "location_longitude":"123.123123", "location_latitude":"45.45454","location_address":"XX省XX市XX街道XX小区"}''',
            # 'data': '''{"xmqkb":{"id":"4a4ce9d6725c1d4001725e38fbdb07cd"},"location_address":"浙江省XX市XX街道XX社区",
            # "location_longitude":"123.123123","location_latitude":"32.32132","c1":"36.9℃以下","c2":"健康","c17":"否",
            # "c4":"否","c5":"否","c6":"否","c18":"正常","c7":"否","type":"YQSJCJ"}''',
            'msgUrl': '''syt/zzapply/list.htm?type=YQSJCJ&xmid=4a4ce9d6725c1d4001725e38fbdb07cd''',
            'uploadFileStr': '''{}''', 'multiSelectData': '''{}'''}
        # Notice: "location_longitude" should be like "123.123123", and "location_latitude" should be like "32.32132"
        # data = '''{{'xmqkb':{"id":"4a4ce9d6725c1d4001725e38fbdb07cd"},"location_address":"",
        # "location_longitude":"","location_latitude":"","c1":"36.9℃以下","c2":"健康","c17":"否","c4":"否","c5":"否",
        # "c6":"否","c18":"正常","c7":"否","type":"YQSJCJ"},'msgUrl':
        # "syt/zzapply/list.htm?type=YQSJCJ&xmid=4a4ce9d6725c1d4001725e38fbdb07cd",'uploadFileStr': "{}",
        # 'multiSelectData': "{}"}}'''
        while True:
            try:
                r = self.session.request('POST', url='https://stu.cugb.edu.cn:443/syt/zzapply/operation.htm',
                                         headers=self.headers, cookies=self.cookies, data=data, verify=False)
                # print(r.status_code)
                if r.text == 'success':
                    self.message2 = 'Clocking-in status: Succeeded'
                    self.subj = '☛已提交每日健康信息...'
                    self.content = """
                    ✔今日打卡成功！
                    """
                elif r.text == 'Applied today':
                    self.message2 = 'Clocking-in status: Applied today'
                    self.subj = '☛健康信息今日已提交！'
                    self.content = """
                    ⚠已经打卡啦！
                    """
                else:
                    self.message2 = 'Clocking-in status: Failed. Please check it'
                    self.subj = '☛出现异常，请查看日志！'
                    self.content = """
                    ✘出错啦，请检查！
                    """
            except Exception as e:
                self.message2 = 'Error Code 1: ' + str(e)
                self.subj = '☛出现异常，请查看日志！'
                self.content = """
                【⚠警告！抛出异常代码！⚠】
                %s
                """ % self.message2
            else:
                break

    def send_to_wechat(self):
        api = "https://sc.ftqq.com/[Your API code].send"
        data = {
            "text": self.subj,
            "desp": self.content}
        requests.post(api, data=data, verify=False)


if __name__ == '__main__':
    student = STUPost()
    student.login()
    # iMessage.send_Message(News=student.message1 + "\n" + student.message2,
    #                      sub="FucknCoVReport: " + student.message2)
    student.send_to_wechat()
