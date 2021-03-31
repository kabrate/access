import time
import webbrowser
import os
import datetime
import requests
#连接wifi
def openwifi():
    os.system('netsh wlan connect name=ncst.edu.cn')
    time.sleep(1)

post_addr="http://172.30.0.11/eportal/InterFace.do?method=login"
post_header={  
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Content-Length': '955',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; servicesJsonStr=2019218103%40%25%25username%40%25%25%E6%A0%A1%E5%9B%AD%E7%BD%91%40%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF; EPORTAL_COOKIE_USERNAME=2019218103; EPORTAL_COOKIE_PASSWORD=192234; EPORTAL_COOKIE_SERVER=%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF; EPORTAL_COOKIE_SERVER_NAME=%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_USER_GROUP=2019%E5%B1%8A%E7%A0%94%E7%A9%B6%E7%94%9F; JSESSIONID=54960D41004FBFEBDE84F73C4958DAFD',
'DNT': '1',
'Host': '172.30.0.11',
'Origin': 'http://172.30.0.11',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://172.30.0.11/eportal/index.jsp?wlanuserip=e84730a45dd2bbfa3cadd7bce89147b1&wlanacname=cee24f8cac61aac974e74b503c3a1669&ssid=&nasip=8618724f96768bd61edb375c4c21ccc0&snmpagentip=&mac=40f3d2d9da8d85bad2b0db6af4e3cab5&t=wireless-v2&url=ee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb&apmac=&nasid=cee24f8cac61aac974e74b503c3a1669&vid=22fa067bbac6d541&port=e68d0a3d42b73226&nasportid=85280d0376cea3452d735fa7f3f2db8de5dd8ab3e13a687f0d08a8da30c78ae7ee0029cf7a78b0d5',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
post_data={
'userId': '2019218103',
'password': '477ddea17d405b0ebea6d3c2d5c97f70487564acf1b5b6d0ddb2d9f68ab4aed659ddfbe04cc8aba2fe50744b2a393784280efe80d2299aae5efe37f7c51c0e86fb05e02a0afa3ddc18877ec180b38870c8c0d92be75cd15ea7b032fd96c7c40f0d63809c8b0c7869e49f5d4c1539dd06927cbf79c2970826ed6120aa938a4536',
'service': '%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF',
'queryString': 'wlanuserip%3De84730a45dd2bbfa3cadd7bce89147b1%26wlanacname%3Dcee24f8cac61aac974e74b503c3a1669%26ssid%3D%26nasip%3D8618724f96768bd61edb375c4c21ccc0%26snmpagentip%3D%26mac%3D40f3d2d9da8d85bad2b0db6af4e3cab5%26t%3Dwireless-v2%26url%3Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%26apmac%3D%26nasid%3Dcee24f8cac61aac974e74b503c3a1669%26vid%3D22fa067bbac6d541%26port%3De68d0a3d42b73226%26nasportid%3D85280d0376cea3452d735fa7f3f2db8de5dd8ab3e13a687f0d08a8da30c78ae7ee0029cf7a78b0d5',
'operatorPwd': '',
'operatorUserId': '',
'validcode': '',
'passwordEncrypt': 'true',
    }

while True:
    print('打开wifi')
    openwifi()
    time.sleep(3)
    print('发送连接请求')
    z=requests.post(post_addr,data=post_data,headers=post_header)
    time.sleep(3)
    now_time = datetime.datetime.now()
    print(str(now_time) + ' 已连接!')
    time.sleep(3600)






