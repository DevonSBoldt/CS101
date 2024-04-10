"""
Help the Finch robot navigate a maze.

CS 101, Lab12, maze.py
Name: Devon Boldt
"""

import finch
import time

# connect to the Finch robot
robot = finch.Finch()

# keep running until done
done = False
while not done:

    #Movement Commands
    def moveFor(): 
    robot.led(,0,255) 
    robot.wheels(1.0,1.0)
    time.sleep(1.0)

    def moveBak():
    robot.led(,0,255)
    robot.wheels(-1.0,-1.0)
    time.sleep(1.0)

    def right():
    robot.led(0,255,0)
    robot.wheels(0.75,-0.75)
    time.sleep(1.0)

    def left():
    robot.led(0,255,0)
    robot.wheels(-0.75,0.75)
    time.sleep(1.0)
    
    # read current sensor values
    left_light, right_light = robot.light()
    left_obstacle, right_obstacle = robot.obstacle()

    # did it just get too dark?
    if left_light < 0.25 and right_light < 0.25:
        done = True

    # RED: is something in the way?
    elif left_obstacle
        left() 
    elif right_obstacle:
        right()
        
      #  robot.led(255, 0, 0)
      #  robot.wheels(-0.75, -0.75)
      #  time.sleep(0.50)

    # GREEN: all clear, move ahead!
    else:
        robot.led(0, 255, 0)
        robot.wheels(1.0, 1.0)
        time.sleep(1)

# grand finale
robot.buzzer(1.5, 10000)
robot.halt()






"""
Help the Finch robot navigate a maze.

CS 101, Lab12, maze.py
Name: Devon Boldt
"""

import finch
import time

# connect to the Finch robot
robot = finch.Finch()

        #Movement Commands
def moveFor(): 
    robot.led(0,0,255) 
    robot.wheels(1.0,1.0)
    time.sleep(1.0)
def moveBack():
    robot.led(0,0,255)
    robot.wheels(-1.0,-1.0)
    time.sleep(1.0)

def right():
    robot.led(255,0,0)
    robot.wheels(0.75,-0.75)
    time.sleep(1.0)

def left():
    robot.led(255,0,0)
    robot.wheels(-0.75,0.75)
    time.sleep(1.0)


# keep running until done
done = False
while not done:
    
    # read current sensor values
    left_light, right_light = robot.light()
    left_obstacle, right_obstacle = robot.obstacle()

    # did it just get too dark?
    if left_light < 0.25 and right_light < 0.25:
        done = True

    # RED: is something in the way?
    if left_obstacle and right_obstacle:
        moveBack()
        right()
    elif left_obstacle:
        left() 
    elif right_obstacle:
        right()
        
      #  robot.led(255, 0, 0)
      #  robot.wheels(-0.75, -0.75)
      #  time.sleep(0.50)

    # GREEN: all clear, move ahead!
    else:
        robot.led(0, 255, 0)
        robot.wheels(1.0, 1.0)
        time.sleep(1)

# grand finale
robot.buzzer(1.5, 10000)
robot.halt()


"""
Help the Finch robot navigate a maze.

CS 101, Lab12, maze.py
Name: Devon Boldt
"""

import finch
import time

# connect to the Finch robot
robot = finch.Finch()

#Movement Commands
def moveFor(): 
    robot.led(0,0,255) 
    robot.wheels(1.0,1.0)
    time.sleep(1.0)
    
def moveBack():
    robot.led(0,0,255)
    robot.wheels(-1.0,-1.0)
    time.sleep(1.0)

def right():
    robot.led(255,0,0)
    robot.wheels(0.75,-0.75)
    time.sleep(1.0)

def left():
    robot.led(255,0,0)
    robot.wheels(-0.75,0.75)
    time.sleep(1.0)


# keep running until done
done = False
while not done:
    
    # read current sensor values
    left_light, right_light = robot.light()
    left_obstacle, right_obstacle = robot.obstacle()

    # did it just get too dark?
    if left_light < 0.25 and right_light < 0.25:
        done = True

    # RED: is something in the way?
    if left_obstacle and right_obstacle:
        moveBack()
        right()
    elif left_obstacle:
        left() 
    elif right_obstacle:
        right()
        
      #  robot.led(255, 0, 0)
      #  robot.wheels(-0.75, -0.75)
      #  time.sleep(0.50)

    # GREEN: all clear, move ahead!
    else:
        robot.led(0, 255, 0)
        robot.wheels(1.0, 1.0)
        time.sleep(1)

# grand finale
robot.buzzer(1.5, 10000)
robot.halt()


"""
Help the Finch robot navigate a maze.

CS 101, Lab12, maze.py
Name: Devon Boldt
"""

import finch
import time

# connect to the Finch robot
robot = finch.Finch()

#Movement Commands
def moveFor(): 
    robot.led(0,0,255) 
    robot.wheels(0.25,0.25)
    time.sleep(0.5)
    
def moveBack():
    robot.led(0,0,255)
    robot.wheels(-0.25,-0.25)
    time.sleep(0.5)

def right():
    robot.led(255,0,0)
    robot.wheels(0.25,-0.25)
    time.sleep(0.5)

def left():
    robot.led(255,0,0)
    robot.wheels(-0.25,0.25)
    time.sleep(0.5)


# keep running until done
done = False
while not done:
    
    # read current sensor values
    left_light, right_light = robot.light()
    left_obstacle, right_obstacle = robot.obstacle()

    # did it just get too dark?
    if left_light < 0.25 and right_light < 0.25:
        done = True

    # RED: is something in the way?
    if left_obstacle and not right_obstacle:
        right()
    elif right_obstacle and not left_obstacle:
        left()
    elif left_obstacle and right_obstacle:
        moveBack()
        right()

    # GREEN: all clear, move ahead!
    else:
        robot.led(0, 255, 0)
        robot.wheels(1.0, 1.0)
        time.sleep(1)

# grand finale
robot.buzzer(1.5, 10000)
robot.halt()


"""
Help the Finch robot navigate a maze.

CS 101, Lab12, maze.py
Name: Devon Boldt
"""

import finch
import time

# connect to the Finch robot
robot = finch.Finch()

#Movement Commands
def moveFor(): 
    robot.led(0,0,255) 
    robot.wheels(0.25,0.25)
    time.sleep(0.5)
    
def moveBack():
    robot.led(0,0,255)
    robot.wheels(-0.6,-0.6)
    time.sleep(0.5)

def right():
    robot.led(255,0,0)
    robot.wheels(0.4,-0.4)
    time.sleep(0.5)

def left():
    robot.led(255,0,0)
    robot.wheels(-0.4,0.4)
    time.sleep(0.5)


# keep running until done
done = False
turntry = 1
while not done:
    # read current sensor values
    left_light, right_light = robot.light()
    left_obstacle, right_obstacle = robot.obstacle()

    # did it just get too dark?
    if left_light < 0.25 and right_light < 0.25:
        done = True

    # RED: is something in the way?
    if left_obstacle and not right_obstacle:
        moveBack()
        right()
    elif right_obstacle and not left_obstacle:
        moveBack()
        left()
    elif left_obstacle and right_obstacle:
        moveBack()
        if turntry > 0:
            left()
        else:
            right()
        turntry = turntry*-1

    # GREEN: all clear, move ahead!
    else:
        robot.led(0, 255, 0)
        robot.wheels(0.75, 0.75)
        time.sleep(0.075)

# grand finale
robot.buzzer(5, 440)
robot.halt()


