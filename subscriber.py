#!/usr/bin/env python3
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("127.0.0.1",1883,60)

incoming_file = open("infoming_file_from_queue.txt", "w+")

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  print(msg.payload.decode())
  incoming_file.write(msg.payload.decode())

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

