# PepperRobot-Navigation
Mapping and navigation with Pepper robot
In this program we can create a map, add places that we want to travel between and add voice commands to move the robot. To create the map and find the coordinates of the points in that map we use the program “Map_Places.py”.

## Map_Places.py
### Mapping()
	Place the robot at the origin point. It’s important to mark this point because it’s critical to configurate the “Navig_In_Map.py” program. It’s also critical to render a good map. The quality of the map will depend on the reflection of the ground or walls and the amount of light in the room. Sometimes the robot finds hard to move in places full of light or with a lot of reflections because it uses lasers to map the surroundings.
	After setting the origin, you should define a radius of exploration. Right the radius you want to explore at the correct place of the function. Then run the function Mapping() and wait until the robot maps everything in that radius. In the end the map created will be shown in the computer and in the python console will show the path of the map (the map is stored in the robot). You should save this path for later use. If the map is not good enough repeat the process until it is to your liking. 

### **Places_Position()**
	To use this function first you need to define a path, which you already have from the last function. Paste that path in the right place and get the robot to origin point. Then run the function Places_Config() and wait until the message “Relocalize done” appears on the console. 
	Then place the robot in the place you want to know the coordinates and run Places_Coordinates(). The coordinates of the place will be shown on the console. You should save these points for later use. The point will be shown like this: [[Coordinates], [Uncertainty]]. You should save the coordinates of each point/place.


## Navig_In_Map.py
	
	To get the robot to navigate in the map first you need to place the robot in the origin and then run the Config_Navig() function that will set everything needed for the robot to navigate through the map. You should write the coordinates of the points, the path of the map and the words that should be recognized by the robot in the right places of that function and then launch it. After everything is settled launch the Navig_In_Map() function. Now you can give inputs to the robot (saying something) and when he recognizes the word he will go the respective place, this away you can travel through the map using voice commands. If you say “stop” the robot will stop at the exact same. You can say home and the robot will go to the home position. In this case home position is the origin.

Note 1:  The navigation in Pepper does not consider the angle so when you send the robot to a specific place, the way is going to be place is a bit random, somethings he stops facing a direction and in the other time he’s facing a completely different one. 

Note 2: Bear in mind that the smoothness of the travelling will depend on various factors. For my experience, the quality of the map is crucial for a smooth and accurate navigation and the amount of light in the room affects the lasers of the robot so except some abnormalities with lots of light. 

Note 3: While navigating through the map the robot can avoid obstacles.  

Comments
1-	Getting a good map is one of the most important things that will make the robot to travel smoothly. When making the map look for non-existing edges and for wrong walls or obstacles. Create maps until one is good enough for navigation.
2-	Getting the right coordinates of all points is also very important. Try to navigate through them before running the main app. The navigation does not consider the angles the robot is facing so the robot will be facing random positions every time you navigate to a point.
3-	I had to decrease the security distances to navigate better 
4-	The robot can avoid obstacles when navigating but make sure he can pass considering the security distances. If not, he will stop and it wont work. 
5-	In tight spaces the edges of the wall will make him move side by side to avoid the “invisible walls” that he mapped. 
6-	The app works better with low light conditions. Sometimes reflections or sunlight can affect navigation and exploration, putting “walls” where they don’t exist.
