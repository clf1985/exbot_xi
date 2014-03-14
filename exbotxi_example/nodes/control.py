#!/usr/bin/env python
# coding=utf-8
#
# Author: Yuanbo She yuanboshe@126.com
# Group: ExBot http://blog.exbot.net
#
# Software License Agreement (BSD License)
#
# Copyright (c) 2014, ExBot.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import rospy
from geometry_msgs.msg import Twist

def control():
    topic = "/cmd_vel_mux/input/teleop" # 发布的topic名，如果使用仿真机器人请改为"/cmd_vel"
    rospy.init_node('exbotxi_example_control')
    cmdVelPub = rospy.Publisher(topic, Twist)
    
    rospy.loginfo("exbot_example_control python start...")
    speed = Twist()
    while not rospy.is_shutdown():
        speed.linear.x = 0.2; # 设置线速度为0.2m/s，正为前进，负为后退
        speed.angular.z = 0.5; # 设置角速度为0.5rad/s，正为左转，负为右转
        cmdVelPub.publish(speed) # 将刚才设置的指令发送给机器人
        
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass