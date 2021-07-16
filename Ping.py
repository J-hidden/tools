from pythonping import ping

# 需要在Terminal中以sudo运行
response = ping('8.8.8.8', count=15)
print(response)
# 以秒为单位
print('最大延迟为：%s秒' % response.rtt_max)
print('最小延迟为：%s秒' % response.rtt_min)
print('平均延迟为：%s秒' % response.rtt_avg)
# 以毫秒为单位
print('平均延迟为：%s毫秒' % response.rtt_avg_ms)
print('最小延迟为：%s毫秒' % response.rtt_min_ms)
print('最大延迟为：%s毫秒' % response.rtt_max_ms)
print('丢包数为：%s毫秒' % response.packet_loss)
