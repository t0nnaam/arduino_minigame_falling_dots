from kiddeemata import kiddeemata, OUTPUT, INPUT
import random
import sys
import time
from tkinter import *
from datetime import datetime

board = kiddeemata.KiddeeMata()
board.OLED_start()
time.sleep(1)

joystick = board.joystickStart()
time.sleep(1)

x = 0
y = 0

item = [0x39,
        0x39,
        0x39,
        0x39,
        0x00,
        0x00,
        0x00,
        0x00]

itemCounter = 0
itemSpeed = 0.2

y1 = 0
x1 = random.randrange(0,15,1)

state1 = False
state2 = False
CSelect = False
start = False

hit = False
lives = 3
    

while(1):
    joystick.update()
    RawMoveLeftRight = joystick.leftStickX
    print ("Move Left/right: ", RawMoveLeftRight)
    RawMoveUpDown = joystick.rightStickY
    print ("Move up/down: ", RawMoveUpDown)
        
    if joystick.buttonX:
        print ("x")
    if joystick.buttonStart:
        start = True
    if joystick.buttonY:
        print ("Y")
    if joystick.buttonB:    
        board.OLED_drawImage('kirby.png', x, y, resize = [32,32])
        state1 = True
        state2 = False
        CSelect = True
    if joystick.buttonA:
        board.OLED_drawImage('espurr.png', x, y, invert = True, resize=[32,32])
        state2 = True
        state1 = False
        CSelect = True
    
    def drawitem():
        board.OLED_setCursor (x1, y1)
        board.OLED_drawTile(item)

    def checkHit():
        global lives
        if (y==y1 and x<=x1<=(x+4)):
            lives -=1
            hit = True
            print ("hit")
            print (lives, " lives")
            
    def drawLife():
        if (lives == 3):
            board.OLED_drawImage('life.png', 11, 1, invert = True, resize = [8,8])
        if (lives >= 2):
            board.OLED_drawImage('life.png', 13, 1, invert = True, resize = [8,8])
        if (lives >= 1):
            board.OLED_drawImage('life.png', 15, 1, invert = True, resize = [8,8])

    while(start == True and CSelect == True):
        joystick.update()
        RawMoveLeftRight = joystick.leftStickX
        print ("Move Left/right: ", RawMoveLeftRight)
        RawMoveUpDown = joystick.rightStickY
        print ("Move up/down: ", RawMoveUpDown)

        drawLife()
        
        drawitem()
        time.sleep(itemSpeed)
        #board.OLED_clearDisplay()
        board.OLED_clearLine(y1)
        
        checkHit()

        if (y1 == 7) or (hit == True):
            y1=0
            x1 = random.randrange(0,15,1)
            if  hit == False:
                itemCounter+= 1
                if (itemSpeed-0.005) > 0:
                    itemSpeed = itemSpeed - 0.005
            drawLife()
            hit = False
        else:
            y1+=1
        
        if (state1 == True) :
            board.OLED_drawImage('kirby.png', x, y, resize = [32,32])
            while (RawMoveLeftRight > 0 and x < 12) :
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveLeftRight = joystick.leftStickX
                print ("Move Left/right: ", RawMoveLeftRight)
                x+=1
                time.sleep(0.1)

            while (RawMoveLeftRight < 0 and x > 0) :
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveLeftRight = joystick.leftStickX
                print ("Move Left/right: ", RawMoveLeftRight)
                x-=1
                time.sleep(0.1)

            while (RawMoveUpDown > 0 and y < 5):
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveUpDown = int (joystick.rightStickY)
                print(y)
                y+=1
                time.sleep(0.1)
                
            while (RawMoveUpDown < 0 and y > 0):
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveUpDown = int (joystick.rightStickY)
                print(y)
                y-=1
                time.sleep(0.1)


        if (state2 == True) :
            board.OLED_drawImage('espurr.png', x, y, invert = True, resize=[32,32])
            while (RawMoveLeftRight > 0 and x < 12) :
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveLeftRight = joystick.leftStickX
                print ("Move Left/right: ", RawMoveLeftRight)
                x+=1
                time.sleep(0.05)

            while (RawMoveLeftRight < 0 and x > 0) :
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveLeftRight = joystick.leftStickX
                print ("Move Left/right: ", RawMoveLeftRight)
                x-=1
                time.sleep(0.05)

            while (RawMoveUpDown > 0 and y < 5):
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveUpDown = int (joystick.rightStickY)
                y+=1
                time.sleep(0.05)

            while (RawMoveUpDown < 0 and y > 0):
                board.OLED_clearDisplay()
                joystick.update()
                RawMoveUpDown = int (joystick.rightStickY)
                y-=1
                time.sleep(0.05)
                
        if (lives == 0):
            board.OLED_clearLine(1)
            break
        
    time.sleep(0.1)

    if (lives == 0):
        print ("")
        print ("Game Over")
        print ("Score: ",itemCounter) 
        print ("")
        break
