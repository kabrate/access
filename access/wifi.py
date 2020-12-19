import pywifi
import time
import os
import requests
#保存包中写义的常量
from pywifi import const

def wifi_connect_status():
    """
    判断本机是否有无线网卡,以及连接状态
    :return: 已连接或存在无线网卡返回1,否则返回0
    """
    #创建一个元线对象
    wifi = pywifi.PyWiFi()

    #取当前机器,第一个元线网卡
    iface = wifi.interfaces()[0] #有可能有多个无线网卡,所以要指定

    #判断是否连接成功
    if iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
        print('wifi已连接')
        return 1
    else:
        print('wifi未连接')
    return 0

def scan_wifi():
    """
    扫苗附件wifi
    :return: 扫苗结果对象
    """
    #扫苗附件wifi
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan() #扫苗附件wifi
    time.sleep(1)
    basewifi = iface.scan_results()
    for i in basewifi:
        print('wifi扫苗结果:{}'.format(i.ssid)) # ssid 为wifi名称
        print('wifi设备MAC地址:{}'.format(i.bssid))
    return basewifi


def connect_wifi():
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
    print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(3)  # 缓冲3秒


    profile = pywifi.Profile()  # 配置文件
    profile.ssid = "ncst.edu.cn"  # wifi名称
    #profile.auth = const.AUTH_ALG_OPEN  # 需要密码
    profile.auth = const.AUTH_ALG_SHARED #无需密码
    #profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
    #profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    #profile.key = '4000103000' #wifi密码

    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件

    ifaces.connect(tmp_profile)  # 连接
    time.sleep(10)  # 尝试10秒能否成功连接
    isok = True
    if ifaces.status() == const.IFACE_CONNECTED:
        print("成功连接")
    else:
        print("失败")
    #ifaces.disconnect()  # 断开连接
    time.sleep(1)
    return isok

def openwifi():
    os.system('netsh wlan connect name=ncst.edu.cn')
    time.sleep(1)

def login():
    thedata={'domain':'CMCC',
           'enablemacauth':'0',
           'password':'xxxx',
           'username':'batt1ebear'
          }
    theheader={
    'Host': 'a.nuist.edu.cn',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://a.nuist.edu.cn/index.php?url=aHR0cDovL2RldGVjdHBvcnRhbC5maXJlZm94LmNvbS9zdWNjZXNzLnR4dA==',
    'Content-Length': '67',

    'Cookie':'_gscu_1147341576=059821653286gq10; sunriseUsername=123441534;\
    sunriseDomain=NUIST;sunriseRememberPassword=true; sunrisePassword=123456;\
    PHPSESSID=hb0o9bkct2f6ge164oj3vj0me5;think_language=zh-CN',
    'Connection':'keep-alive',
}

    url="http://a.nuist.edu.cn/index.php/index/login"
    p=requests.post(url,data=thedata,headers=theheader)

print(wifi_connect_status())

#openwifi()