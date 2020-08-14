import base64
import requests

username = '2005190059'
userpwd = '972833'
eusername = str(base64.b64encode(username.encode('utf-8')), 'utf-8')
euserpwd = str(base64.b64encode(userpwd.encode('utf-8')), 'utf-8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2575 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/4039 MicroMessenger/7.0.17.1720(0x27001137) Process/tools WeChat/arm64 NetType/WIFI Language/en ABI/arm64',
    'Referer': 'http://stu.cugb.edu.cn/webApp/xuegong/index.html',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
print(eusername)
print(euserpwd)

url = "http://stu.cugb.edu.cn"
session = requests.session()
session.get(url)
html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
cookie = 'JSESSIONID' + '=' + str(html_set_cookie['JSESSIONID']) + ';' + 'token' + '=' + str(html_set_cookie['token'])
headers['Cookie'] = cookie
print(html_set_cookie)
print(headers)

def get_token():  # 在公共变量进行方法传参，添加相应变量，否则不添加
    # 获取token：调用get_token方法
    # token_url = "http://***********m/initiator/live/get-token"
    # token_data = {"activityId": "******"}
    # token_headers = {"Cookie": "vmpbId=*******1935d5323cda6"}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2575 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/4039 MicroMessenger/7.0.17.1720(0x27001137) Process/tools WeChat/arm64 NetType/WIFI Language/en ABI/arm64',
        'Referer': 'http://stu.cugb.edu.cn/webApp/xuegong/index.html',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}  # ,
    gettoken = re.search(r'(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', login.text)
    t = requests.post('http://stu.cugb.edu.cn', headers=headers)
    return t


# a = get_token()
# print(a)