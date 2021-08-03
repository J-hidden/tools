from  netmiko  import ConnectHandler
import sys
import time
from datetime import datetime
import os

#获取当前的年月日
file_time = time.strftime("%Y-%m-%d", time.localtime())
##创建实时时间文件夹
def mkdir(file_name):
    folder = os.path.exists(file_name)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(file_name)  # makedirs 创建文件时如果路径不存在会创建这个路径

mkdir(file_time)

#通过这个函数可以切割各个部分然后通过循环赋值给每一个变量
f = open('ip2.txt', 'r', encoding='UTF-8')
line = 'A'
print('正在采集设备配置，请稍等。。。')
while line != "":
    line = f.readline()
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    while line:
        a = line.split()
        ip = a[:1]
        username = a[1:2]
        password = a[2:3]
        line = f.readline()
        device = ConnectHandler(device_type='huawei', ip=ip[0], username=username[0], password=password[0])
        output = device.send_command('dis cu')
        file_name = open('%s/%s-%s.log' % (file_time, ip[0], time), "w+")
        print(output, file=file_name, flush=True)
        #print(output, file=sys.stdout)
        print('已采集%s' % ip[0])
        device.disconnect()
    f.close()
    print('已全部采集成功')