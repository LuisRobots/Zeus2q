# https://www.systemtechnologyworks.com/

import aiml
import pyaudio
import subprocess
import time
import os
import sys
import speech_recognition as sr 
from os import environ, path
import random
import datetime
import wikipedia
import maestro
from multiprocessing import Process
from subprocess import run, PIPE



servo = maestro.Controller()

power = 'on'



text = ''

aiml_dir = "/home/zeus/speech/alice/"
zeus = aiml.Kernel()
zeus.learn(os.sep.join([aiml_dir, '*.aiml']))
properties_file = open(os.sep.join([aiml_dir, 'bot.properties']))
for line in properties_file:
     parts = line.split('=')
     key = parts[0]
     value = parts[1]
     zeus.setBotPredicate(key, value)
zeus.respond("load aiml b")

c = sr.Recognizer()

def on():
    servo.setTarget(17,3000)

def off(): 
    servo.setTarget(17,7000)

def armSpeed(n):
    
    servo.setSpeed(0,n)
    servo.setSpeed(1,n)
    servo.setSpeed(2,n)
    servo.setSpeed(3,n)
    servo.setSpeed(4,n)
    servo.setSpeed(6,n)
    servo.setSpeed(7,n)
    servo.setSpeed(8,n)
    servo.setSpeed(9,n)
    servo.setSpeed(10,n)
    servo.setSpeed(12,n)
    servo.setSpeed(13,n)
	

def acceleration(a):
   
    servo.setAccel(0,a)
    servo.setAccel(1,a)
    servo.setAccel(2,a)
    servo.setAccel(3,a)
    servo.setAccel(4,a)
    servo.setAccel(6,a)
    servo.setAccel(7,a)
    servo.setAccel(8,a)
    servo.setAccel(9,a)
    servo.setAccel(10,a)
    servo.setAccel(12,a)
    servo.setAccel(13,a)


def standBy():

    servo.setTarget(0,5000)
    servo.setTarget(1,4000)
    servo.setTarget(2,1000)
    servo.setTarget(3,9000)
    servo.setTarget(4,10000)
    servo.setTarget(6,1000)
    servo.setTarget(7,10000)
    servo.setTarget(8,9000)
    servo.setTarget(9,2000)
    servo.setTarget(10,1000)
    servo.setTarget(12,6000)
    servo.setTarget(13,6000)
    time.sleep(3)

    
def srMove(): # small random moves
	
	armSpeed(10)

	servo.setTarget(0,random.randrange(1000,6000))
	servo.setTarget(1,random.randrange(1000,6000))
	servo.setTarget(2,random.randrange(1000,5000))
	servo.setTarget(3,random.randrange(5000,9000))
	servo.setTarget(4,random.randrange(7000,10000))
	servo.setTarget(6,random.randrange(1000,6000))
	servo.setTarget(7,random.randrange(1000,10000))
	servo.setTarget(8,random.randrange(6000,9000))
	servo.setTarget(9,random.randrange(2000,5000))
	servo.setTarget(10,random.randrange(1000,5000))
	servo.setTarget(12,random.randrange(5000,7000))
	servo.setTarget(13,random.randrange(4000,8000))
	time.sleep(3)
	servo.setTarget(12,6000)
	servo.setTarget(13,6000)
	time.sleep(2)

	
   
def nodding():
	servo.setSpeed(12,30)
	servo.setTarget(12,6000)
	time.sleep(.5)
	servo.setTarget(12,5000)
	time.sleep(.5)
	servo.setSpeed(12,30)
	servo.setTarget(12,6000)

	


def HeadMove(): # small head random moves
	servo.setTarget(12,random.randrange(5500,6500))
	servo.setTarget(13,random.randrange(4000,7000))
	time.sleep(1)
	servo.setTarget(12,6000)
	servo.setTarget(13,6000)

def voice (audio):
    subprocess.run (['espeak','-s 110', '-a 800', '-p 50', audio])
    time.sleep(1.5)

def respond (inVoice):
	text = zeus.respond(" %s" % inVoice)
	voice (text)
	
		

def wiki():
	voice ("What would you like to serch in wikipedia")
	search = audioProcess()
	info = wikipedia.summary(search, 2)
	voice (info)
        



def keyword():
	
	power = 'on'

	command = audioProcess()
	print(command)
	try:
		
		if 'off' in command:
			print('Power off')
			power = 'off'
			
		elif 'time' in command:
			time = datetime.datetime.now().strftime('%I:%M %p')
			voice ("Current time is" + time)
			

		elif "who's" in command:
			search = command.replace("who's", '')
			info = wikipedia.summary(search, 2)
			voice (info)
			
		elif 'who' in command:
			search = command.replace('who is', '')
			info = wikipedia.summary(search, 2)
			voice (info)
			
		else:
			# voice_data = audioProcess()
			respond (command)
			print('Processing')
			
	except:
		pass

	return power	
			

def audioProcess():
	text = ''
	try:
		with sr.Microphone() as source:
			print('Adjusting for ambient noise')
			c.adjust_for_ambient_noise(source, duration=1)
			
			print('listening...')
			
			caudio = c.listen(source)
			text = c.recognize_google(caudio)
			print(text)
			
		
	except:
		pass

	return text	
			

def presentation():
   
    voice ("Hello humans")
    
    voice ("My name is zeus and I'm here on the behalf of humanoid robots")
    
    voice ("I was designed for research and STEM education. I have simple parts")
    
    voice ("wait, what are the parts i forgot let me think")
    time.sleep(2)
    
    voice ("oh ok I remember I have servo motors and lot of wires ")
   
    voice ("and remember a controller board and a video camera so I can see you and measure your distance")

    voice ("I might have a sound card with a microphone so be careful I can be listening to everything you say  ")

    voice ("I think there is a computer to help me remember and proccess information")

    voice ("I wonder if the computer is working because I can not remember anything")

    voice ("Ok I think I need a reboot")
    time.sleep(2)
    voice ("give me a second")
   # move.stop()
    standBy()
    servo.setTarget(12,4000)
    time.sleep(5)
    standBy()

def present():

    move = Process(target=moveloop, args=())
    pres = Process(target=presentation, args=())
    pres.start()
    move.start()
    pres.join()
    move.join()

def conversation():
    movet = Process(target=moveC, args=())
    conv = Process(target=keyword, args=())
    conv.start()
    conv.join()
    movet.start()
    movet.join()


def moveC():
    srMove()
    HeadMove()
    standBy()
      


def moveloop():
    i = 1
    while i < 12:
        srMove()
        time.sleep(2)
        i += 1
    standBy()

def check_distance_threshold():
    output = run('./rs-distance/rs-distance', stdout=PIPE)
    output_str = output.stdout.decode("utf-8")
    distances = []
    for line in output_str.split('\n')[5:-1]:
        distance = line.split(' ')[6]
        distances.append(float(distance))
    print(distances)
    return sum(distances) / len(distances) < 1.5

                                              # JEDI
def clench_lightsaber():
    armSpeed(0)
    servo.setTarget(0, 8000)
    time.sleep(1)
    servo.setTarget(0, 5000)
    armSpeed(10)


def jedi_move_1():
    armSpeed(10)
    HeadMove()

    # Bring arm up
    servo.setTarget(2, 3000)
    servo.setSpeed(3, 40)
    servo.setTarget(3, 5000)

    time.sleep(1)

    # Reset from attack position
    servo.setTarget(2, 5000) # Curl elbow up further
    servo.setSpeed(1, 30)
    servo.setTarget(1, 6500) # turn elbow ccw

    voice("Only a Sith deals in absolutes")

    time.sleep(1) # Pause

    # Move shoulder down
    servo.setSpeed(3, 40)
    servo.setTarget(3, 9000)

    servo.setSpeed(1, 40)
    servo.setSpeed(2, 40)
    servo.setTarget(1, 1000) # Bring lightsaber halfway back to start pos

    servo.setTarget(2, 3000) # Make arm straight

    time.sleep(2) # Pause

    HeadMove()

    # Reset
    armSpeed(10)

def jedi_move_2():

    servo.setTarget(7, 14000) # Turn hand up

    servo.setTarget(8, 20)
    servo.setTarget(8, 5000) # lift up forearm

    time.sleep(2)

    servo.setTarget(6, 4500)

    # Catchphrase
    voice("I am one with the Force")
    voice("The Force is with me")

    HeadMove()



def jedi_move_3():
    # Make arm move up slower, come down faster

    HeadMove()

    servo.setSpeed(3, 30)
    servo.setTarget(3, 5000)

    servo.setSpeed(2, 20)
    servo.setTarget(2, 3000)

    servo.setSpeed(4, 50)
    servo.setTarget(4, 5000) # Move shoulder out

    voice("Confronting fear is the destiny of a jedi")

    HeadMove()

    armSpeed(10)

# Open shoulder up all the way and swing using elbow
def jedi_move_4():

    HeadMove()

    # Open shoulder all the way up
    servo.setSpeed(4, 30)
    servo.setTarget(4, 1000)

    # Lift left arm up slightly
    servo.setTarget(9, 6000)

    time.sleep(1.5)

    voice("For the republic!")

    # Close shoulder to default
    servo.setSpeed(4, 60)
    servo.setTarget(4, 10000)

    time.sleep(1)
    
    servo.setSpeed(9, 30)
    servo.setTarget(9, 1000)

    HeadMove()
def jedi():
	
	standBy()
	clench_lightsaber()
	voice ("Zeus 2Q Jedi Mode")
	time.sleep(2)
	clench_lightsaber()


	j = 0
	while j < 1:

		is_activated = check_distance_threshold()

		print(is_activated)
		if is_activated == True:
			voice("Stand back")
			clench_lightsaber()
			time.sleep(1)

			if j == 0:
				jedi_move_1()
				standBy()
			elif j == 1:
				jedi_move_2()
				standBy()
			elif j == 2:
				jedi_move_3()
				standBy()
			elif j == 3:
				jedi_move_4()
				standBy()
		

			clench_lightsaber()
			time.sleep(3)

			j += 1

		voice ('my Jedi senses')
		time.sleep(1)
		voice ('do not sense anyone close to me')

                                                 # RPS

def RPSInit():
    servo.setTarget(6,10000)
    servo.setTarget(8,9000)
    time.sleep(0.3)
    servo.setTarget(8,2000)
    time.sleep(0.3)
    
def Sciccors():
    servo.setTarget(6,1000)
    time.sleep(0.4)
    
def Paper():
    servo.setTarget(7,1000)
    time.sleep(0.4)
    servo.setTarget(6,1000)
    time.sleep(0.4)
    
def Rock():
    servo.setTarget(7,2000)
    servo.setTarget(6,10000)
    time.sleep(0.4)

def rpc():
	standBy()
	armSpeed(0)
	servo.setTarget(9,4000)
	time.sleep(0.3)
	servo.setTarget(6,1000)
	time.sleep(0.3)
	
	g=0
	while g < 5:
		# is_activated = check_distance_threshold()
		# print(is_activated)
		# if is_activated == True:
			list1 = [1, 2, 3]
			prob = random.choice(list1)
			# prob = random.randrange(1,3)
			voicecallRPS = ["Rock", "Paper", "Scissors", "Shoot"]
			interval = 0
			while interval < 4:
				RPSInit()
				voice(voicecallRPS[interval])
				interval += 1
				
			if prob == 3:
				Rock()
				voice ("Rock")
			if prob == 2:
				Paper()
				voice ("Paper")
			if prob == 1:
				Sciccors()
				voice ("Scissors")
			voice("Good Game next")
			standBy()
			time.sleep(10)
			g += 1



a = ''

print('Please enter g to start:')
a = input()
        

voice ("Initializing system now give me a secound")

armSpeed(10)
on()
standBy()
# 
present()
# voice ("I am back Let do a role play")
# jedi()
standBy()

voice ("Let play rock paper Scissors")
rpc()
standBy()

voice ("Let start a coversation ")
voice ("Ask me any question ")
armSpeed(10)
while True:
	pow = keyword()
	if pow == "off":
		break
	else:
		# conversation()
		HeadMove()
		srMove()
		standBy()
		keyword()

		
standBy()		
voice ('powering off good day')	
off()
sys.exit()
