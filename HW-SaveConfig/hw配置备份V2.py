#-*-coding:utf-8-*-
from  netmiko  import ConnectHandler
import sys
import time

#如果每行中有多个字符串，例如ip+用户名+密码+端口，可以使用model_1模块增加

##保存终端输出
class Logger(object):


    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)

    def flush(self):
        pass
#时间格式
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Connect_HW(object):


    #重置类的参数
    def __init__(self, username, password, port=22):
        self.username = username
        self.password = password
        self.port = port

    def Connect(self):
        #打开同路径下的ip.txt文件
        f = open('ip.txt', 'r', encoding='UTF-8')
        line = 'A'
        #赋予line一个初始值，然后循环ip.txt中行进行链接并且记录日志
        #通过ip+时间的格式来作为保存的log文件名称
        #最后关闭链接，关闭文件
        while line != "":
            line = f.readline()
            device = ConnectHandler(device_type='huawei', ip=line, username=self.username, password=self.password)
            output = device.send_command('dis cu')
            print(output)
            sys.stdout = Logger('%s-%s.log' % (line, time), sys.stdout)  # 这里使用标准路径，如果只写文件名称则为当前路径下文件
            device.disconnect()
        f.close()

lixilei = Connect_HW('username','password')
print(lixilei.Connect())