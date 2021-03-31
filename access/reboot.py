import time
import os
import io
import sys
import win32api
import win32con
#按下按键
def key_event(input_key):
    win32api.keybd_event(input_key, 0, 0, 0)#按下
    time.sleep(0.01)
    win32api.keybd_event(input_key, 0, 1, 0)#松开
    time.sleep(0.3)

# 打开一个应用
def open_app(app_dir):
  os.startfile(app_dir)

def end_program(pro_name):
    os.system('%s%s' % ("taskkill /F /IM ", pro_name))

def reboot():
    end_program("SunloginClient.exe")
    time.sleep(10)
    open_app("D:\Sunflower\SunloginClient\SunloginClient.exe")
while True:
    #time.sleep(43200)
    print("开始重置")
    reboot()
    time.sleep(5)
    key_event(37)#按下左键
    time.sleep(3)
    key_event(13)#按下回车
    print("开始计时")
    time.sleep(43200)

