#!/usr/bin/python
#encoding:utf-8
import RPi.GPIO as GPIO         ## 导入GPIO库
import time                     ## 导入time库
pin_sound = 8	## 使用8号引脚

#GPIO.cleanup()                   ## 清除
GPIO.setmode(GPIO.BOARD)        ## 使用BOARD引脚编号
GPIO.setup(pin_sound, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)       ## 设置8号引脚输出

def GetNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

for i in range(0,3):
	#print GetNowTime(),'\t',GPIO.input(pin_sound)
	GPIO.wait_for_edge(pin_sound, GPIO.RISING)
	print GetNowTime(),"high, you can do something"
	time.sleep(1)

GPIO.cleanup()                   ## 清除
