import os
import time
import json
import random
import numpy as np
import paho.mqtt.client as mqtt
import socket

# Constants
ROBOT_ID = int(os.getenv("ROBOT_ID", 0))
SWARM_TOPIC = "swarm/coordinates"
TARGET_POSITION = [50, 50]  # Dynamic Target
connected = False

# Robot's state
position = np.array([random.randint(0, 100), random.randint(0, 100)], dtype=np.float64)
velocity = np.array([0, 0], dtype=np.float64)
swarm_positions = {}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Robot {ROBOT_ID} connected with result code {rc}")
    client.subscribe(SWARM_TOPIC)

def on_message(client, userdata, msg):
    global swarm_positions
    try:
        swarm_positions.update(json.loads(msg.payload.decode()))
    except Exception as e:
        print(f"Error processing message: {e}")

# Movement logic
def compute_velocity():
    global position, velocity
    # Cohesion: Move toward center of swarm
    center = np.mean(list(swarm_positions.values()), axis=0) if swarm_positions else position
    cohesion = center - position

    # Separation: Avoid collisions
    separation = np.zeros(2)
    for pos in swarm_positions.values():
        diff = position - np.array(pos, dtype=np.float64)
        if np.linalg.norm(diff) < 10:
            separation += diff

    # Alignment: Match velocity (simplified as moving toward the target)
    alignment = np.array(TARGET_POSITION, dtype=np.float64) - position

    # Combine forces
    velocity = cohesion * 0.01 + separation * 0.1 + alignment * 0.05
    position[:] += velocity

# MQTT Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
time.sleep(2)
client.connect("mqtt_broker", 1883, 60)

# Main loop
client.loop_start()
#while not connected:
#    try:
#        client.connect("mqtt_broker", 1883, 60)
#        connected = True
#    except socket.error:
#        print("MQTT broker not ready. Retrying in 2 seconds...")
#        time.sleep(2)

while True:
    compute_velocity()
    client.publish(SWARM_TOPIC, json.dumps({ROBOT_ID: position.tolist()}))
    time.sleep(0.1)
