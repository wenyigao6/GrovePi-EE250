#Ultrasonic Sensor Server
#
# This code runs on your VM and receives a stream of packets holding ultrasonic
# sensor data and prints it to stdout. Use a UDP socket here.
import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

from grovepi import *

#use UDP

import socket

def Process1():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '127.0.0.1'
    port = 9005

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Server Started: ")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + data)
    c.close()

if __name__ == '__main__':
    Process1()