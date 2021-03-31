
import time
import os
import datetime
import requests

post_addr="http://cpss.izaodao.com/study/index.html?lessonId=116766#/video"
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
while True:

    z=requests.get(post_addr,data=post_data,headers=post_header)
    time.sleep(3)

    time.sleep(3)






