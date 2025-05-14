#!/usr/bin/python3

print (""" ███▄    █  ▄▄▄        ██████  ██░ ██  ▄▄▄          ██░ ██  ▒█████    ▄████  ▄▄▄       ██▀███  
 ██ ▀█   █ ▒████▄    ▒██    ▒ ▓██░ ██▒▒████▄       ▓██░ ██▒▒██▒  ██▒ ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄     ▒██▀▀██░▒██░  ██▒▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██    ░▓█ ░██ ▒██   ██░░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  
▒██░   ▓██░ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒   ░▓█▒░██▓░ ████▓▒░░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒
░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░  a  ▒ ░░▒░▒░ ▒░▒░▒░  a▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░    ▒ ░▒░ ░  ░ ▒ ▒░   ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░
   ░   ░ ░   ░   ▒   ░  ░  ░   ░  ░░ ░  ░   ▒       ░  ░░ ░░ ░ ░ ▒  ░ ░   ░   ░   ▒     ░░   ░ 
         ░       ░  ░      ░   ░  ░  ░      ░  ░    ░  ░  ░    ░ ░        ░       ░  ░   ░     
                                                                                               """)

import time 
import os
import sys



done = 'false'
#here is the animation
def animate():
    for i in range(3):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rhacking started!     ')

animate()
#long process here
done = 'false'

print('\n')
time.sleep(3)
i = 0
for i in range(100):
	print ("Hacking NASA :", i , "%")
	i += 1
	time.sleep(0.05)
	
print("\033[1mNASA HAVE BEEN HACKED BY NASHA HOGAR")
time.sleep(3)

os.system('cmatrix')