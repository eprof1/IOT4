import paho.mqtt.client as mqtt
import time
import datetime

print("Listening for sensor/timestamp messages from 192.168.1.78")

def on_message(client, userdata, msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Received message on topic '{msg.topic}': {msg.payload.decode()} at {current_time}")

broker_address = "127.0.0.1"
port = 1883
topic = "sensor/timestamp"

client = mqtt.Client()
client.on_message = on_message

client.connect(broker_address, port, 60)
client.subscribe(topic)

try:
    # Start the MQTT client loop in a separate thread
    client.loop_start()

    # Main loop to check for messages every 10 seconds
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Gracefully stop the MQTT client loop on keyboard interrupt (Ctrl+C)
    client.loop_stop()
    print("MQTT client loop stopped.")
