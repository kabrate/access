import time
import os
import io
import sys

# 打开一个应用
def open_app(app_dir):
  os.startfile(app_dir)

def end_program(pro_name):
    os.system('%s%s' % ("taskkill /F /IM ", pro_name))

def reboot():
    end_program("SunloginClient.exe")
    time.sleep(10)
    open_app("E:\Sunflower\SunloginClient\SunloginClient.exe")
while True:
    print("开始计时")
    time.sleep(86400)
    print("开始重置")
    reboot()

