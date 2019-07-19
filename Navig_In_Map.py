# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:23:33 2019

@author: Pedro Oliveira
"""

import time
from naoqi import ALProxy
import threading


class Navig(): 
    
    def Config_Navig(self): #Configurates all the initial things to be used in the main app
        self.Robot_IP = "172.16.0.77"
        self.Navigation = ALProxy("ALNavigation", self.Robot_IP, 9559)
        self.Posture = ALProxy("ALRobotPosture", self.Robot_IP, 9559)
        self.Motion = ALProxy("ALMotion", self.Robot_IP, 9559)
        self.ASR = ALProxy("ALSpeechRecognition", self.Robot_IP, 9559)
        self.Memory = ALProxy("ALMemory", self.Robot_IP, 9559)
        self.Blinking = ALProxy("ALAutonomousBlinking", self.Robot_IP, 9559)
        self.Listening = ALProxy("ALListeningMovement", self.Robot_IP, 9559)
        self.Speak = ALProxy("ALTextToSpeech", self.Robot_IP, 9559)
        self.SpeakMov = ALProxy("ALSpeakingMovement", self.Robot_IP, 9559)
        self.AnimSpeech = ALProxy("ALAnimatedSpeech", self.Robot_IP, 9559)
        self.Localization = ALProxy("ALLocalization", self.Robot_IP, 9559)
    
        self.xL = -0.6642232537269592   #Coordinates of point 1 - In this case, Laboratory 
        self.yL = -3.749622106552124
        self.ThetaL = -2.7310893535614014
 
        self.xE = 4.968353271484375 #Coordinates of point 2 - In this case, Entrance
        self.yE = 0.6844285130500793
        self.ThetaE = -0.07399776577949524
      
        self.xS =  -1.6242592334747314  #Coordinates of point 3 - In this case, Stairs
        self.yS = -0.22312086820602417
        self.ThetaS = -2.4569268226623535
     
        #self.ASR.unsubscribe("Test_ASR") #Activate this function only when an erro occurs. When the speech recognition is activated you need to use this, when it's not, don't use this. By default it's unsubscribed.
        #self.Navigation.stopExploration()
        
        self.Navigation.stopLocalization()   #Sets the languange and the words that should be recognized by the robot
        self.ASR.setLanguage("English")
        self.vocabulary1 = ["Laboratory", "Entrance", "Stairs", "Stop", "Home", "Pepper"] 
        self.ASR.setVocabulary(self.vocabulary1, False)
        
        self.Motion.setOrthogonalSecurityDistance(0.20)  #Sets the security distance for the sensors 
        self.Motion.setTangentialSecurityDistance(0.03)  
        self.Motion.setExternalCollisionProtectionEnabled("Arms", False)
        
        self.Blinking.setEnabled(True)
        self.Listening.setEnabled(True)
        
        self.SpeakMov.setEnabled(True)
        self.configuration = {"bodyLanguageMode":"contextual"} 
          
        
        self.Motion.wakeUp()
        self.path = "/home/nao/.local/share/Explorer/2019-07-09T083744.926Z.explo" #path of the map (previously made) - Paste your path here
        self.Navigation.loadExploration(self.path) #loads the map
        self.Navigation.getMetricalMap()
        self.Navigation.startLocalization()
        self.Navigation.relocalizeInMap([0, 0, 0]) #Setting the origin, must be known by the user. It's the point where the exploration started when the map was made - origin
        self.Navigation.navigateToInMap([self.xE, self.yE, self.ThetaE]) #Place where the user wants the robot to stay waiting for input
        self.Navigation.wait(self.Navigation.navigateToInMap([self.xE, self.yE, self.ThetaE]), 1)
        self.Posture.goToPosture("StandInit", 0.5)
        self.Navigation.stopLocalization()
          

    def Navigation_Process(self):
        print "Thread1 started"
        self.Posture.goToPosture("StandInit", 0.5)
        self.Navigation.startLocalization()
        self.Navigation.getMetricalMap() 
        self.AnimSpeech.say("Hello! Where do you want to go?", self.configuration)
        print "First Checkpoint"
        while True:
            
            if self.Word[1] >= 0.400 and self.Word[0] == 'Laboratory':  #Recognitio2n of words and moving to the point after receiving the word input
                self.Navigation.startLocalization()
                print "Lab Checkpoint 1"
                Moving_Lab = self.Navigation.navigateToInMap([self.xL, self.yL, self.ThetaL])
                self.Navigation.wait(Moving_Lab, 1)
                self.AnimSpeech.say("Welcome to the lab", self.configuration)
                self.ASR.unsubscribe("Test_ASR")
                self.Posture.goToPosture("StandInit", 0.5)
                print "Lab Checkpoint 2"
                self.ASR.unsubscribe("Test_ASR")
                time.sleep(2)
                
            if self.Word[1] >= 0.400 and self.Word[0] == 'Entrance':
                self.Navigation.startLocalization()
                print "Entrance Checkpoint 1"
                Moving_Lab = self.Navigation.navigateToInMap([self.xE, self.yE, self.ThetaE])
                self.Navigation.wait(Moving_Lab, 1)
                self.AnimSpeech.say("Thanks for coming!", self.configuration)
                self.ASR.unsubscribe("Test_ASR")
                self.Posture.goToPosture("StandInit", 0.5)
                print "Entrance Checkpoint 2"
                self.ASR.unsubscribe("Test_ASR")
                time.sleep(2)    
                    
            if self.Word[1] >= 0.400 and self.Word[0] == 'Stairs':
                self.Navigation.startLocalization()
                print "Stairs Checkpoint 1"
                Moving_Lab = self.Navigation.navigateToInMap([self.xS, self.yS, self.ThetaS])
                self.Navigation.wait(Moving_Lab, 1)
                self.AnimSpeech.say("Thanks for coming!", self.configuration)
                self.ASR.unsubscribe("Test_ASR")
                self.Posture.goToPosture("StandInit", 0.5)
                print "Stairs Checkpoint 2"
                self.ASR.unsubscribe("Test_ASR")
                time.sleep(2) 
           
    
     
    def Home_Process(self):  #Function to stop the robot when he recognizes "stop" and goes back to origin 
        print "Thread2 started"
        
        while True:
            time.sleep(1)
            self.ASR.subscribe("Test_ASR")
            self.Word = self.Memory.getData("WordRecognized")
            print("Word: ") 
            print(self.Word)
            
            if self.Word[1]  >= 0.400 and self.Word[0] == 'Pepper':
                print "Pepper recognized"
                self.Process2.start()
                self.ASR.unsubscribe("Test_ASR")
             
            if self.Word[1] >= 0.400 and self.Word[0] == 'Stop':
                self.Navigation.navigateToInMap(self.Navigation.getRobotPositionInMap()[0])
                self.ASR.unsubscribe("Test_ASR")
                print "Stoped"
                
            if self.Word[1] >= 0.500 and self.Word[0] == 'Home':
                self.Navigation.startLocalization()
                Moving_Lab = self.Navigation.navigateToInMap([0.0, 0.0, 0.0])
                self.Navigation.wait(Moving_Lab, 1)
                self.Navigation.stopLocalization()
                self.ASR.unsubscribe("Test_ASR")
                print "Home"
                break
   
    def Navig_In_Map(self):
        self.Process1 = threading.Thread(target=self.Home_Process)
        self.Process2 = threading.Thread(target=self.Navigation_Process)  
        #self.Thread1.daemon = True
        

        self.Process1.start()
        time.sleep(5)            
        self.Process1.join()
               
        print "Completed"
       
    
    
      
    
