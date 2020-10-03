# coding:utf-8
import requests
from http import cookiejar
import time
import iMessage
import base64
import datetime
import random

class PCPost:
    def __init__(self):
        self.cookies = {}
        # mock the build-in browser of WeChat:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2575 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/4039 MicroMessenger/7.0.17.1720(0x27001137) Process/tools WeChat/arm64 NetType/WIFI Language/en ABI/arm64',
            'Referer': 'http://stu.cugb.edu.cn/webApp/xuegong/index.html',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}#,
            #'Content-Length': '783'}
        # mock the others
        # self.headers ={'User-Agent': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}
        self.session = requests.session()
        self.message1 = ''
        self.message2 = ''
        self.message3 = ''

    def login(self):
        try:
            #Request the cookie and token from the origin web:
            originurl = 'http://stu.cugb.edu.cn'
            req = self.session.get(originurl)
            set_cookie = requests.utils.dict_from_cookiejar(req.cookies)
            header_cookie = 'JSESSIONID' + '=' + str(set_cookie['JSESSIONID']) + ';' + 'token' + '=' + str(set_cookie['token'])
            #Add the cookie and token into headers:
            self.headers['Cookie'] = header_cookie
            url = 'http://stu.cugb.edu.cn//login/Login.htm'
            uname = 'example'  # Your Student Number, e.g. 2001200001
            upwd = 'example'  # You ID card: last 6 numbers, e.g. 123456
            # A new feature for the site that uses base64 encoding for the username and password, and uses token:
            uname_encrypt = str(base64.b64encode(uname.encode('utf-8')), 'utf-8')
            upwd_encrypt = str(base64.b64encode(upwd.encode('utf-8')), 'utf-8')
            token = str(set_cookie['token'])
            data = {'username': uname_encrypt, 'password': upwd_encrypt, 'verification': '', 'token': token}
            req = self.session.post(url=url, data=data, headers=self.headers)
            time.sleep(10)
            # cookies = requests.utils.dict_from_cookiejar(req.cookies)
            # for key in cookies:
            #     cookie = ""
            #     cookie = cookie + key + "=" + str(cookies[key])
            # cookie = cookie + "; username=example; menuVisible=0" # For example: 200119000X (Your Student Number)
            # The link used in the bulit-in browser of WeChat：
            content = self.session.post(
                'http://stu.cugb.edu.cn/webApp/xuegong/index.html#/zizhu/apply?projectId=4a4ce9d674438da101745ca20e2b3a5e&type=YQSJCJ')
            # The Link used in the web browsers (random stamp/timestamp exists, unresolved):
            # content = self.session.post('http://stu.cugb.edu.cn:80/syt/zzapply/apply.htm?type=yqsjcj&judge=sq&xmid=4a4ce9d6725c1d4001725e38fbdb07cd&_t=809439&_winid=w6236')
            if content.status_code == 200:
                self.message1 = "Login status: Succeeded"
                time.sleep(10)
                self.out_apply()
            else:
                self.message1 = "Login status: Failed"
        except Exception as e:
            self.message1 = 'Error Code 0: ' + str(e)
            
    def random_reason(self):
        Y = datetime.datetime.now().year
        M = datetime.datetime.now().month
        D = datetime.datetime.now().day + 1
        if D < 10:
        	date = str(Y) + "-" + str(M) + "-" + "0" + str(D)
        else:
        	date = str(Y) + "-" + str(M) + "-" + str(D)
        reas_addr = {"买日用品" : "民族园路2号",
						 "买水果" : "学清路27号",
						 "牙医预约" : "花园北路49号",
						 "出去吃饭" : "中关村北大街127号",
						 "健身锻炼" : "中关村东路16号",
						 "买衣服" : "三里屯路19号",
						 "购物" : "成府路28号",
						 "购买东西" : "中关村西区善缘街1号",
						 "雅思培训" : "中关村大街19号",
						 "户外锻炼" : "科荟路33号",
						 "呼吸新鲜空气" : "科荟路33号",
						 "户外运动" : "科荟路33号",
						 "修发理发" : "学清路甲8号"}
        reas, addr = random.choice(list(reas_addr.items()))
        return (reas, date, addr)
				
    def out_apply(self):
        #cookie_para = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        (reas, date, addr) = self.random_reason()
        datastr = '''{"xmqkb":{"id":"4a4ce9d674438da101745ca20e2b3a5e"},"location_address":"北京市海淀区学院路街道中国地质大学(北京)","location_longitude":"116.36211","location_latitude":"39.952298","c1":"139XXXXXXXX","c2":"临时出校","c17":"学19楼","c18":"1103","c7":\"%s\","c8":\"%s\","c13":\"%s\","c15":"是","type":"YQSJCJ"}'''
        data = {
            'data': datastr % (reas, date, addr),
            'msgUrl': '''syt/zzapply/list.htm?type=YQSJCJ&xmid=4a4ce9d674438da101745ca20e2b3a5e''',
            'uploadFileStr': '''{"c16":}''',
            'multiSelectData': '''{}'''}
        # Notice: "location_longitude" should be like "123.123123", and "location_latitude" should be like "32.32132"
        # data = '''{{'xmqkb':{"id":"4a4ce9d6725c1d4001725e38fbdb07cd"},"location_address":"","location_longitude":"","location_latitude":"","c1":"36.9℃以下","c2":"健康","c17":"否","c4":"否","c5":"否","c6":"否","c18":"正常","c7":"否","type":"YQSJCJ"},'msgUrl': "syt/zzapply/list.htm?type=YQSJCJ&xmid=4a4ce9d6725c1d4001725e38fbdb07cd",'uploadFileStr': "{}",'multiSelectData': "{}"}}'''
        try:
            r = self.session.request('POST', url='http://stu.cugb.edu.cn/syt/zzapply/operation.htm',
                                     headers=self.headers, data=data)
            #print(r.status_code)
            if r.text == 'success':
                self.message2 = 'Succeeded'
                self.message3 = reas + "\n" + date + "\n" + addr
            elif r.text == 'Applied today':
                self.message2 = 'Applied today'
                self.message3 = reas + "\n" + date + "\n" + addr
            else:
                self.message2 = 'Failed. Please check it'
        except Exception as e:
            self.message2 = 'Error Code 1: ' + str(e)

if __name__ == '__main__':
    student = PCPost()
    student.login()
    iMessage.send_Message(News=student.message1 + "\n" + "Out-Apply: " + student.message3,
                          sub="Application: " + student.message2)