# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:20:16 2019

@author: Pedro Oliveira
"""

#This code is used to Map any place in a pre defined radius and to save coordinates of points within the map

import time
from PIL import Image
import numpy as np
from naoqi import ALProxy

Navigation = ALProxy("ALNavigation", "172.16.0.77", 9559)
Posture = ALProxy("ALRobotPosture", "172.16.0.77", 9559)
Motion = ALProxy("ALMotion", "172.16.0.77", 9559)

    
def Mapping():
    Radius = 8 #Choose the radius you want to use for the exploration
    time.sleep(30)

    Motion.wakeUp()  #Wakes up the robot, if it's awaken does nothing
    Motion.setOrthogonalSecurityDistance(0.25) #These two lines sets the security distances os the robot
    Motion.setTangentialSecurityDistance(0.04)
    
    error = Navigation.explore(Radius)
    if error != 0:
        print "Mapping failed"
    else:
        print "Mapping done"
    time.sleep(2)
    
    path = Navigation.saveExploration() #saves the previous exploration
    print(path) #prints the path of the file which contains the map previously created
    
    Navigation.startLocalization() 
    Navigation.navigateToInMap([0, 0, 0]) #Returns to the starting point. The robot not always goes to the exact same point as it started because of variations. But the right origin position is where you started the exploration.
    Navigation.stopLocalization()
    Posture.goToPosture("StandInit", 0.5) 

    Final_map = Navigation.getMetricalMap()
    data = Final_map[4] #gets the data of the map 
    size = Final_map[1] #size of the map
    size2 = Final_map[2] #size of the map
    img = np.array(data).reshape(size, size2)
    img = (100 - img) * 2.5   #shapes the image to fit the map
    img = np.array(img, np.uint8)
    NewMap = Image.frombuffer('L',  (size, size2), img, 'raw', 'L', 0, 1)
    NewMap.show() #Shows the map on the computer


class Places_Function():  
    def Places_Config(self):
        Navigation.stopLocalization()
        self.path = "/home/nao/.local/share/Explorer/2019-07-09T083744.926Z.explo" #Paste the path of the map here
        
        Motion.setOrthogonalSecurityDistance(0.3)
        Motion.setTangentialSecurityDistance(0.06)
        Loading = Navigation.loadExploration(self.path)
        print(Loading) #True if successful
    
        Navigation.getMetricalMap()
        Navigation.startLocalization()
        Navigation.relocalizeInMap([0, 0, 0]) #start at home position (defined by the user)
        print "Relocalize done"
        
    def Places_Coordinates(self): #Place the robot in the right position and then run this
        print(Navigation.getRobotPositionInMap()) #get the position of the robot in the map
        Posture.goToPosture("StandInit", 0.5)
        Navigation.stopLocalization()
        print "Coordinates done"
    

    
    

    
    





























































