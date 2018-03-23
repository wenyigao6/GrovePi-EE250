"""EE 250L Lab 07 Skeleton Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time

from grovepi import *

global led
led = 4

pinMode(led, "OUTPUT")


def led_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    # print("custom_callback: " + message.topic + " " + "\"" + 
    #     str(message.payload, "utf-8") + "\"")
    # print("custom_callback: message.payload is of type " + 
    #       str(type(message.payload)))

    if str(message.payload, "utf-8") == str("LED_ON", "utf-8"):
        # do sth
        digitalWrite(led, 1)

    elif str(message.payload, "utf-8") == str("LED_OFF", "utf-8"):
        # do sth
        digitalWrite(led, 0)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi8/led")
    client.message_callback_add("anrg-pi8/led", led_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    message = client.on_connect

    while True:
        # print("delete this line")
        time.sleep(1)


        # if message == "LED_ON":
        #     # turn led on

        # elif message == "LED_OFF":
        #     # turn led off 
            
        # message = client.on_connect

        # # client.publish("anrg-pi8/ultrasonicRanger", dist)
