#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import RPi.GPIO as GPIO

left1 = 16
left2 = 18
right1 = 12 
right2 = 10

def motor(speed,PIN2,p):
        
    if speed >= 0.0:
        p.ChangeDutyCycle(speed * 100.0)
        GPIO.output(PIN2,True)
    else:
        p.ChangeDutyCycle(-speed * 100.0)
        GPIO.output(PIN2,False)
               
def callback(data):

    LR = data.axes[0]
    FR = data.axes[1]

    cR = FR / 2.5 + LR / 6.0
    cL = FR / 2.5 - LR / 6.0

    motor(cR, right2, pr)
    motor(cL, left2, pl)
    
#    print "FR LR"

def listener():
    global pr 
    global pl
 
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(left1, GPIO.OUT)
    GPIO.setup(left2, GPIO.OUT)
    GPIO.setup(right1, GPIO.OUT)
    GPIO.setup(right2, GPIO.OUT)

    pr = GPIO.PWM(right1, 500.0)
    pl = GPIO.PWM(left1, 500.0)
    pr.start(0)
    pl.start(0)

    rospy.init_node('motor_out', anonymous=True)

    rospy.Subscriber('joy', Joy, callback)

#    motor(0.4, right2, pr)
#    motor(0.66, left2, pl)
    
    try:
        rospy.spin()
#    except KeyboardInterrupt:
    finally: 
        print "stopping...."
        pr.stop()
        pl.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    listener()
