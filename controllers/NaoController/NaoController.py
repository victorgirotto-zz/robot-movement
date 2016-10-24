# File:          NaoController.py
# Date:          
# Description:   
# Author:        
# Modifications: 

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
#
# or to import the entire module. Ex:
#  from controller import *
from controller import Robot
from controller import Motion

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions
class NaoController (Robot):
  
  timeStep = 128
  
  def initialization(self):
    self.keyboardEnable(self.timeStep)
 
  
  # User defined function for initializing and running
  # the NaoController class
  def run(self):
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')    
    self.initialization()
    walk_motion = Motion("../../motions/Forwards50.motion")
      
    # Main loop
    while True:
      # Perform a simulation step of 64 milliseconds
      # and leave the loop when the simulation is over  
      
      k = self.keyboardGetKey()
      if \k==ord('A'):
        print('Moving forward...')
        walk_motion.play()  
      
      if self.step(self.timeStep) == -1:
        break
        
      
      
      # Read the sensors:
      # Enter here functions to read sensor data, like:
      #  val = ds.getValue()
      
      # Process sensor data here.
      
      # Enter here functions to send actuator commands, like:
      #  led.set(1)
    
    # Enter here exit cleanup code

# The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.
controller = NaoController()
controller.run()
