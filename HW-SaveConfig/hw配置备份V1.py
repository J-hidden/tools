from  netmiko  import ConnectHandler
import sys,time

##保存日志
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

f = open('ip.txt', 'r', encoding='UTF-8')
line = 'A'
while line !=" ":
    line = f.readline()

    ##登入设备，使用命令查询
    device = ConnectHandler(device_type = 'huawei', ip = line , username= 'username', password = 'password')
    output = device.send_command('display cu')
    print(output)
    sys.stdout = Logger('%s-%s.log'% (line,time), sys.stdout)  # 这里使用标准路径，如果只写文件名称则为当前路径下文件
    sys.stderr = Logger('%s-%s.log_file'% (line,time), sys.stderr)
f.close()