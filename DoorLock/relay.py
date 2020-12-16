import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) //GPIO의 핀 번호를 BCM모드로 참조
GPIO.setup(18,GPIO.OUT) //18 GPIO 핀의 출력 설정

GPIO.output(18,True) // 출력모드로 설정된 핀에 True값을 할당
print "power_in" 
time.sleep(2) //2초동안 정지

GPIO.cleanup() // 핀 설정을 초기화
