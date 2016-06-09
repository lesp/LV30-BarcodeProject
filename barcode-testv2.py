import subprocess
import time
import easygui as eg
from gpiozero import TrafficLights
import pygame
import pygame.mixer
from random import randint

def audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)

def numbergame():
    number = randint(1,5)
    guess = 0
    while guess != number:
        guess = eg.enterbox(title="I'm thinking of a number between 1 and 10",msg="What number am I thinking of? \nHere is a hint, when doubled it is"+str((number*2))) 
        guess = int(guess)
        audio("/home/pi/wrong.wav")
    else:
        audio("/home/pi/correct.wav")

def flashing_LED():
    lights = TrafficLights(2, 3, 4)
    lights.green.on()

    for i in range(2):
        time.sleep(10)
        lights.green.off()
        lights.amber.on()
        time.sleep(1)
        lights.amber.off()
        lights.red.on()
        time.sleep(10)
        lights.amber.on()
        time.sleep(1)
        lights.green.on()
        lights.amber.off()
        lights.red.off()

def quiz():
    Q = eg.enterbox(title="Question 1",msg="What is the name for the brass pins on a Raspberry Pi \nA: GPIO B: ASCII C: ESA D: PSU")
    if Q != "A":
        audio("/home/pi/wrong.wav")
    else:
        audio("/home/pi/correct.wav")

while True:
    play = eg.enterbox(title="Would you like to play a game?", msg="Would you like to play a game?")
    while play == "YES":
        audio("/home/pi/correct.wav")
        code = eg.enterbox(title="Please scan a barcode to start",msg="Please scan a barcode to start")
        if code == "MINECRAFT":
            print(code)
            subprocess.call(["minecraft-pi"])
            break
        elif code == "SONIC PI":
            print(code)
            subprocess.call(["sonic-pi"])
            break
        elif code == "LED FLASH":
            print(code)
            flashing_LED()
            break
        elif code == "NUMBER GAME":
            numbergame()
            break
        elif code == "QUIZ":
            quiz()
            break
    else:
        audio("/home/pi/wrong.wav")
        break
        
        
        
    
        

