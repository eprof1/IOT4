# PgP 12/12/2023 create/publish GrovePi data to mqtt
# this works, now add sensor reading each minute

import paho.mqtt.client as mqtt
import time

#PgP add temperature reading libraries
from grovepi import *
import grovepi
import datetime


dht_sensor_port = 5        # Digital Port for DHT sensor
dht_sensor_type = 0        # use 0 for the blue-colored sensor and 1 for the white-colored sensor


def on_publish(client, userdata, mid):
    print(f"Message published to topic: {topic}")

broker_address = "127.0.0.1"
port = 1883
topic = "sensor/timestamp"
message = "waiting for reading"  # Replace with your actual temperature value once inside loop

client = mqtt.Client()
client.on_publish = on_publish

client.connect(broker_address, port, 10)

while True:
    #[temp,hum] = dht(dht_sensor_port,dht_sensor_type)
    #temperature = str(int(temp * 9 / 5 + 32))
    #humidity = str(int(hum))
    #print("Temperature is ", temperature, "degrees Fahrenheit, Humidity is ", humidity, " percent")    
    #message = temperature
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = current_time
    
    result = client.publish(topic, payload=message, qos=1)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"timestamp Message sent successfully at {current_time} ")
    else:
        print(f"Failed to send message. Error: {result.rc}")

    time.sleep(10)  # Wait for 10 seconds before publishing the next message
