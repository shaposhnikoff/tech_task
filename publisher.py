#!/usr/bin/env python3
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("127.0.0.1",1883,60)
with open('requirements.txt') as file:
   for line in file:
       print(line)
       client.publish("topic/test", line);
       if 'str' in line:
          break
client.disconnect();

