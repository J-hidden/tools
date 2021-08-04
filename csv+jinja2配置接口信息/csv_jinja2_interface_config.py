import csv
from jinja2 import Template
from netmiko import ConnectHandler

# 打开CSV文件以及jinja2模板，值得注意的是jinja2模板的光标需要放到下一行，放在最后一行容易导致'keep_trailing_newline=True'无效
csv_file = open('接口配置文件.csv')
template_file = open('interface_templates.j2')

# 将CSV文件内容转化为dict（字典）类型
reader = csv.DictReader(csv_file)
# 通过jinja2中的模板类型打开jinja2模板，keep_trailing_newline=True是让每一个模板结束后自动换行，不然容易第二个模板的第一行与第二个模板的最后一行连接在一起
interface_template = Template(template_file.read(), keep_trailing_newline=True)

interface_configs = ''
# 将CSV中的信息读取并且写成一个列表
for read in reader:
    interface_config = interface_template.render(
        interface=read['interface'],
        description=read['description'],
        vlan=read['vlan']
    )
    interface_configs += interface_config

# netmiko连接交换机的信息，也可以通过文件读取
dev_info = {
    'ip': '192.168.1.1',
    'username': 'lixilei',
    'password': 'python3',
    'device_type': 'huawei'
}
# 通过\n来判断不同的将interface_configs拆解成一个个列表
config_set = interface_configs.split('\n')

conn = ConnectHandler(**dev_info)
print('已连接到交换机')
output = conn.send_config_set(config_set, cmd_verify=False)
'''
cmd_verify=False注解：同Netmiko 2不一样，Netmiko 3中默认要等到输入的命令在屏幕上打印出来后才会执行后面的命令
（因为Netmiko 3默认将send_config_set()里的"cmd_verify"参数设为True)，
像我们这种一次性对交换机输入多达60多条命令的情况（12个端口要配置），
经常会出现网络延迟的问题导致在执行脚本时Netmiko会返回
“netmiko.sshexception.NemikoTimeoutException：Time-out reading channel, data not available”这个异常
（我们写的代码本身没有问题，这是Netmiko 3自身的一个"bug"）
'''
print(output)
