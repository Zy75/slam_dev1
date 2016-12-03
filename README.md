
ORB_SLAM2 test using RPi2 car with camera
[Monocular visual slam]

LAPTOP: ubuntu14.04

RPi2 : ubuntu14.04

Joystick control RPi2 car ----> camera on RPi2 car moves -----> ORB_SLAM2 runs 

note:

1. Video compression is an additional heavy load on RPi2. Don't compress in camera driver. Use [image_transport republish] because it runs in a new thread and another CPU core on RPi2 could be used.  

2. ORB_SLAM2 loses track often, though relocation is possible. The car can only move forward, backward and rotation. Is this charasteristic not suitable for monocular visual slam?  
 
3. Accessing RPi's GPIO needs root and simple [sudo rosrun] doesn't work.  I've finally found how to do it. See run_motor.sh.  

