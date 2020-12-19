import pywifi
import requests
import webbrowser
import os
import time
def openwifi():
    os.system('netsh wlan connect name=ncst.edu.cn')
    time.sleep(1)

#登录地址
post_addr="http://172.30.0.11/eportal/InterFace.do?method=login"
#构造头部信息
#post_header={   
#'Host': '172.30.0.11',
#'Content-Length': '930',
#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#'DNT': '1',
#'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#'Accept': '*/*',
#'Origin': 'http://172.30.0.11',
#'Referer': 'http://172.30.0.11/eportal/index.jsp?wlanuserip=e84730a45dd2bbfa3cadd7bce89147b1&wlanacname=cee24f8cac61aac974e74b503c3a1669&ssid=&nasip=8618724f96768bd61edb375c4c21ccc0&snmpagentip=&mac=40f3d2d9da8d85bad2b0db6af4e3cab5&t=wireless-v2&url=ee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb&apmac=&nasid=cee24f8cac61aac974e74b503c3a1669&vid=22fa067bbac6d541&port=e68d0a3d42b73226&nasportid=85280d0376cea3452d735fa7f3f2db8de5dd8ab3e13a687f0d08a8da30c78ae7ee0029cf7a78b0d5',
#'Accept-Encoding': 'gzip, deflate',
#'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#'Cookie': 'EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_USERNAME=2019118101; EPORTAL_COOKIE_PASSWORD=090955; servicesJsonStr=2019118101%40%25%25username%40%25%25%E7%A7%BB%E5%8A%A8PPPoE%40%E6%A0%A1%E5%9B%AD%E7%BD%91; EPORTAL_COOKIE_SERVER=%E7%A7%BB%E5%8A%A8PPPoE; EPORTAL_COOKIE_SERVER_NAME=%E7%A7%BB%E5%8A%A8PPPoE; EPORTAL_USER_GROUP=2019%E5%B1%8A%E7%A0%94%E7%A9%B6%E7%94%9F; JSESSIONID=F05C62A6F1C642F0103DF41C2EE21DBD',
#'Connection': 'close',
#}
post_header={  
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Content-Length': '930',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; servicesJsonStr=2019118101%40%25%25username%40%25%25%E7%A7%BB%E5%8A%A8PPPoE%40%E6%A0%A1%E5%9B%AD%E7%BD%91; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_USERNAME=2019118101; EPORTAL_COOKIE_PASSWORD=090955; EPORTAL_COOKIE_SERVER=%E7%A7%BB%E5%8A%A8PPPoE; EPORTAL_COOKIE_SERVER_NAME=%E7%A7%BB%E5%8A%A8PPPoE; EPORTAL_USER_GROUP=2019%E5%B1%8A%E7%A0%94%E7%A9%B6%E7%94%9F; JSESSIONID=CDC4B9F58FB2CE975D0EE0BF1C9BEE0A',
'DNT': '1',
'Host': '172.30.0.11',
'Origin': 'http://172.30.0.11',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://172.30.0.11/eportal/index.jsp?wlanuserip=e84730a45dd2bbfa3cadd7bce89147b1&wlanacname=cee24f8cac61aac974e74b503c3a1669&ssid=&nasip=8618724f96768bd61edb375c4c21ccc0&snmpagentip=&mac=40f3d2d9da8d85bad2b0db6af4e3cab5&t=wireless-v2&url=ee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb&apmac=&nasid=cee24f8cac61aac974e74b503c3a1669&vid=b88deea85c347dcc&port=e68d0a3d42b73226&nasportid=85280d0376cea3452d735fa7f3f2db8d847ba13fee4b9e646e9fcfa1fe676f7bca160adbc986eafb',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
#构造登录数据
#post_data='serId=2019118101&password=87a0bfd7926df43b28eafdbcd7eba6e8d5878e4f730342c03a37c99c28334ec602db07d10d6c9c8096e39260a449dfece10a2584df67f6806182bc0ec43da67ecf9534d4575d161045e4c4e603bdc9c021fc904497202d3ca4a53979d0ae4d5bb0e4175b72218234741d666c1d04e1d1b93decb3be0642db2f15bef8601d3375&service=%25E7%25A7%25BB%25E5%258A%25A8PPPoE&queryString=wlanuserip%253De84730a45dd2bbfa3cadd7bce89147b1%2526wlanacname%253Dcee24f8cac61aac974e74b503c3a1669%2526ssid%253D%2526nasip%253D8618724f96768bd61edb375c4c21ccc0%2526snmpagentip%253D%2526mac%253D40f3d2d9da8d85bad2b0db6af4e3cab5%2526t%253Dwireless-v2%2526url%253Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%2526apmac%253D%2526nasid%253Dcee24f8cac61aac974e74b503c3a1669%2526vid%253D22fa067bbac6d541%2526port%253De68d0a3d42b73226%2526nasportid%253D85280d0376cea3452d735fa7f3f2db8de5dd8ab3e13a687f0d08a8da30c78ae7ee0029cf7a78b0d5&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=true'
post_data={
'userId': '2019118101',
'password': '87a0bfd7926df43b28eafdbcd7eba6e8d5878e4f730342c03a37c99c28334ec602db07d10d6c9c8096e39260a449dfece10a2584df67f6806182bc0ec43da67ecf9534d4575d161045e4c4e603bdc9c021fc904497202d3ca4a53979d0ae4d5bb0e4175b72218234741d666c1d04e1d1b93decb3be0642db2f15bef8601d3375',
'service': '%E7%A7%BB%E5%8A%A8PPPoE',
'queryString': 'wlanuserip%3De84730a45dd2bbfa3cadd7bce89147b1%26wlanacname%3Dcee24f8cac61aac974e74b503c3a1669%26ssid%3D%26nasip%3D8618724f96768bd61edb375c4c21ccc0%26snmpagentip%3D%26mac%3D40f3d2d9da8d85bad2b0db6af4e3cab5%26t%3Dwireless-v2%26url%3Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%26apmac%3D%26nasid%3Dcee24f8cac61aac974e74b503c3a1669%26vid%3Db88deea85c347dcc%26port%3De68d0a3d42b73226%26nasportid%3D85280d0376cea3452d735fa7f3f2db8d847ba13fee4b9e646e9fcfa1fe676f7bca160adbc986eafb',
'operatorPwd': '',
'operatorUserId': '',
'validcode': '',
'passwordEncrypt': 'true',
    }
#发送post请求登录网页
openwifi()
time.sleep(3)
webbrowser.open("http://172.30.0.11")
time.sleep(3)
z=requests.post(post_addr,data=post_data,headers=post_header)

