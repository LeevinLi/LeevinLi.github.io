#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @Date   : 2021/6/25
# @Author : jin.li

from time import sleep
import os

# 设备号
DEVICES_ID = 'H812X69801234567'
# 测试次数
NUMBER_OF_TESTS = 5
# 等待时长 = 30(s)
TIME_CALL_WAITING = 20
# 通话间隔 = 60(s)
TIME_CALL_SPACING = 60
# 测试号码
call_num_list = [
                # 垃圾
                '13052208992',
                '19117036924',
                '13127798020',
                '18255091131',
                '15026879029',
                '18217210992',
                '15576152251',
                '13585674724',
                '18721996107',
                '18221577697',
                '19945689943',
                '13671601186',
                '13248044303']


# 拨打电话
def call_phone(number):
    # 拨打电话
    call = os.popen('adb -s {} shell am start -a android.intent.action.CALL -d tel:{}'.format(DEVICES_ID, number))
    sleep(TIME_CALL_WAITING)

    # 挂断电话
    # 点击挂断按钮，需按不同机型进行坐标适配，不需要亮灭屏
    hangUp = os.popen('adb shell input tap 550 2100')

    # 操作前先在设置里打开power键可以结束通话按钮，否则会导致代码报错
    # hangUp = os.popen('adb shell input keyevent KEYCODE_ENDCALL')
    sleep(TIME_CALL_SPACING)


# 循环拨出电话
index = 1
while index <= NUMBER_OF_TESTS:
    for num in call_num_list:
        print('>>>>>>>>>>>>>>> About to call: ', num)
        call_phone(num)
        index += 1
        print('>>>>>>>>>>>>>>> End to call: ', index)
