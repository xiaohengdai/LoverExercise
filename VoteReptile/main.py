import os
import time
from threading import Thread
import uiautomator2 as u2

device_id = "SSGUGAFAFUTCZ9PF"
apk_name = "UCBrowser.apk"
package_name = "com.UCMobile"
url = "https://bytedance.feishu.cn/docs/doccnvQcoT7phC8l9RwnVuwHxcf#i2kMQn"
pwd = "mt123456"

dir = os.getcwd()
print("dir:", dir)
apk_path = os.path.join(dir, apk_name)

d = u2.connect_usb(device_id)

install_apk_cmd = f"adb -s {device_id} install {apk_path}"


#oppo手机安装apk时需要开线程处理输入密码等弹窗
def input_pw():
    d.set_fastinput_ime(True)
    time.sleep(2.0)
    # 等待弹窗出现
    d.send_keys(pwd)
    d(text="安装").click()
    time.sleep(6.0)
    # 点击输入密码
    #d(text="安装").click()
    d.click(0.5,0.95)


# 安装apk&并输入密码弹窗
a_thread = Thread(target=input_pw)
a_thread.setDaemon(True)
a_thread.start()
os.system(install_apk_cmd)

#启动uc浏览器app并处理权限弹窗
d.app_start(package_name)
d(text="同意并开启服务").click()
d(text="允许").click()
d(text="允许").click()
d(text="允许").click()
time.sleep(8.0)

#点击搜索框并输入飞书投票url,修复开源框架中的一个输入法初始化容易超时失败的一个Bug
d(description="搜索框").click()
d.set_fastinput_ime(True)
time.sleep(7)
d.send_keys(url)

# d(focused=True).set_text(url)
time.sleep(3)
try:
    d(text="进入").click()
except:
    pass
finally:
    print(111)
    d.set_fastinput_ime(False)
d.implicitly_wait(10.0)

#滑动到小楠楠投票处
n = 15
for i in range(0, n):
    print("str(i+1):"+str(i+1))
    d.swipe(0.5, 0.9, 0.5, 0.1)
    time.sleep(5)

#进行投票
x0=917


d.click(x0, 416)
time.sleep(3)

d.click(x0, 525)
time.sleep(3)

d.click(x0, 571)
time.sleep(3)

d.click(x0, 754)
time.sleep(3)

#投票按钮主要在以上四个区域出现


# #卸载apk
uninstall_apk_cmd=f"adb -s {device_id} uninstall {package_name}"
print("uninstall_apk_cmd:",uninstall_apk_cmd)
os.system(uninstall_apk_cmd)
#
