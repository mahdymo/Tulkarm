import time
import json
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

# Constants
SWARM_TOPIC = "swarm/coordinates"
positions = {}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker.")
    client.subscribe(SWARM_TOPIC)

def on_message(client, userdata, msg):
    global positions
    try:
        positions.update(json.loads(msg.payload.decode()))
    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_start()

# Visualization
plt.ion()
fig, ax = plt.subplots()
while True:
    ax.clear()
    for pos in positions.values():
        ax.scatter(pos[0], pos[1], c='blue')
    ax.scatter(50, 50, c='red', marker='x', label="Target")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    plt.pause(0.1)
