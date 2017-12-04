#coding=utf-8
"""
简述：暂停一秒time.sleep()输出；并格式化当前时间。
"""

import time

print('暂停一秒')
time.sleep(1)
print('当前时间为:%s' % time.strftime('%Y-%m-%d %H:%M:%S'))
print('当前时间为:%s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))