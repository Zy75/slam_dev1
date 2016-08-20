#!/bin/sh

rosrun --prefix "sudo -E LD_LIBRARY_PATH=/opt/ros/indigo/lib PYTHONPATH=/opt/ros/indigo/lib/python2.7/dist-packages" motor_out motor_root.py
