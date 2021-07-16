import ipaddress

# 反掩码计算
c1 = ipaddress.ip_network('192.168.1.1/30', strict=False).hostmask
print(c1)