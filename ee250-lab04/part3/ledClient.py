# LED Client 
#
# This code sends requests to the Raspberry Pi to turn on and
#off the Grove LED using TCP packets.

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

from grovepi import *

import time

# Connect the Grove LED to digital port D4
led = 2

pinMode(led,"OUTPUT")
time.sleep(1)

print ("This example will blink a Grove LED connected to the GrovePi+ on the port labeled D4.\nIf you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.\nYou may also try reversing the direction of the LED on the sensor.")
print (" ")
print ("Connect the LED to the port labele D4!" )


import socket

def Main():
    """127.0.0.1 is the loopback address. Any packets sent to this address will
    essentially loop right back to your machine and look for any process 
    listening in on the port specified."""
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1', 5000)


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #by default, the socket constructor creates an TCP/IPv4 socket
    s.bind((host,port))
    s.listen(1)
    c, addr = s.accept()
    while True:
       	data = c.recv(1024).decode('utf-8')
       	
       	if not data:
       		break

       	if data == 'LED_ON'
       		digitalWrite(led,1)

       	if data == 'LED_OFF'
       		digitalWrite(led,0)

       	except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led,0)
        break
	    except IOError:				# Print "Error" if communication error encountered
	        print ("Error")

        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 

    s.close()

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 tcpClient.py` in terminal, this if-statement will be 
true"""
if __name__ == '__main__':
    Main()


ledClient.py
Displaying ledServer.py.