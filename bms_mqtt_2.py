# Send 20 battery data with current timestamp 

import paho.mqtt.client as mqtt
import time, random, threading
import multiprocessing as mp
import time
import random
# client, user and device details
serverUrl   = "103.58.120.8"
clientId    = "bms"
device_name = "bms"
topic="005a00524856501920353154"
interval=60

# display all incoming messages  //// Callback function for subscribe
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(" > Subscribed message: " + payload)

# publish a message
def publish(topic, message, wait_for_ack = False):
    QoS = 2 if wait_for_ack else 0
    message_info = client.publish(topic, message, QoS)
    if wait_for_ack:
        print(" > awaiting ACK for {}".format(message_info.mid))
        message_info.wait_for_publish()
        print(" < received ACK for {}".format(message_info.mid))

# display all outgoing messages  // Callback function for publish
def on_publish(client, userdata, mid):
    print(" < message published ")

# connect the client to server
client = mqtt.Client(clientId)

client.on_message = on_message
client.on_publish = on_publish

client.connect(serverUrl)
client.loop_start()

publish("s/indus", "Device :," + device_name + ",Board", wait_for_ack = True)
print("Device registered successfully!")
client.subscribe(topic)
#client.subscribe(topic1)
# main device loop
# send Temperature,Humidity,Light Intensity measurements
while True :
   
    # Get the current Unix timestamp
    unix_timestamp = int(time.time())
    num_as_string = str(unix_timestamp)
    print(f"Current Unix Timestamp: {unix_timestamp}")
    publish(topic,num_as_string+";CS"+str(round(random.uniform(-5,-20),4))+";"+str(round(random.uniform(35,45),4))+";240.0800;CEVS"+ \
            str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+";"+str(round(random.uniform(11,14),4))+ \
            ";VETS"+str(round(random.uniform(1000,1950),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+";"+str(round(random.uniform(22,49),4))+ \
                          ";TEMS0ME;")
    #publish(topic,num_as_string+";CS15.2655;135.3333;240.0800;CEVS14.2225;12.1410;13.1599;11.8888;11.1245;12.7896;12.5550;11.7582;12.1112;11.7893;14.2225;12.1410;13.1599;11.8888;11.1245;12.7896;12.5550;11.7582;12.1112;11.7893;VETS25.2118;35.2562;30.2572;30.0000;50.7852;55.4455;30.0230;30.8888;30.1450;30.2118;25.2118;35.2562;30.2572;30.0000;50.7852;55.4455;30.0230;30.8888;30.1450;30.2118;TEMS0ME;")
    time.sleep(interval)


   