# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')

# import grovepi

from grovepi import *
# import grovepi

# use TCP

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Server Started")
    while True:
    	data = input("LED_ON or LED_OFF")
    	s.sendto(data.encode('utf-8'),addr)
    c.close()

if __name__ == '__main__':
    Main()