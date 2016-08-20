#!/usr/bin/env python

import yaml
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker

def talker():
    pub = rospy.Publisher("visualization_marker", Marker, queue_size=10)
    rospy.init_node('add_marker', anonymous=True)

    
    with open('/home/pt110/pose.yaml', 'r') as f:
        p = yaml.load(f) 
        px =  p["pose"]["position"]["x"]
        py =  p["pose"]["position"]["y"]
        pz =  p["pose"]["position"]["z"]
      
        ox =  p["pose"]["orientation"]["x"]
        oy =  p["pose"]["orientation"]["y"]
        oz =  p["pose"]["orientation"]["z"]
        ow =  p["pose"]["orientation"]["w"]

        marker = Marker()
        marker.header.frame_id ="/VSLAM";
        marker.header.stamp = rospy.Time.now ()
        marker.ns = "my_namespace"
        marker.id = 0
        marker.action = marker.ADD
        marker.type = marker.CUBE        
        
        marker.pose.position.x = px;
        marker.pose.position.y = py;
        marker.pose.position.z = pz;
        marker.pose.orientation.x = ox;
        marker.pose.orientation.y = oy;
        marker.pose.orientation.z = oz;
        marker.pose.orientation.w = ow; 

        marker.scale.x = 0.1
        marker.scale.y = 0.05
        marker.scale.z = 0.05

        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        r = rospy.Rate(2)

        while not rospy.is_shutdown():
            pub.publish(marker)
            r.sleep()

if __name__ == '__main__':
    talker()
