
import win32api
import time
import win32con
import webbrowser
import os
import io
import sys
import datetime
#鼠标移动
def mouse_move(x,y):
    win32api.SetCursorPos([x,y])

#鼠标点击，默认左键
def mouse_click(click_type="left"):
    if click_type=="left":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)   
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)

#鼠标双击击，默认左键
def mouse_double_click(click_type="left"):
    if click_type=="left":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)



def key_input( input_words=''):
    for word in input_words:
        win32api.keybd_event(VK_CODE[word], 0, 0, 0)
        win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

def key_even( input_key):
    win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.3)

def is_connected(url):
    try:
        host = socket.gethostbyname(url)
        s = socket.create_connection((host, 80), 2)
        return True
    except Exception as e:
        return False


# 是否连接网络
def  isConnected():
  import requests
  try:
        html = requests.get("http://www.baidu.com", timeout=2)
  except:
        return False
  return True

# 关闭其他应用程序
# pro_name:将要关闭的程序
def end_program(pro_name):
    os.system('%s%s' % ("taskkill /F /IM ", pro_name))


# 打开一个应用
def open_app(app_dir):
  os.startfile(app_dir)

def reboot():
    end_program("SunloginClient.exe")
    time.sleep(10)
    open_app("E:\Sunflower\SunloginClient\SunloginClient.exe")

while True:
    t = isConnected()
    print(t)

    # print(t)
    if t == 0:
        mouse_move(1677,1062)
        time.sleep(3)
        mouse_click()
        mouse_move(1641,500)
        time.sleep(3)
        mouse_click()
        mouse_move(1821,615)
        time.sleep(3)
        mouse_click()
        webbrowser.open("http://172.30.0.11")
        mouse_move(1415,580)
        time.sleep(5)
        mouse_click()
        end_program("msedge.exe")
        reboot()
        time.sleep(20)
    else:
        time.sleep(360)
        now_time = datetime.datetime.now()
        time.sleep(5)
        print(now_time)





