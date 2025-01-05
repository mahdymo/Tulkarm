<h1>
  <span style="color:green;">T</span>
  <span style="color:red;">u</span>
  <span style="color:black;">l</span>
  <span style="color:white; background-color:black;">k</span>
  <span style="color:green;">a</span>
  <span style="color:red;">r</span>
  <span style="color:black;">m</span>
</h1>

![Swarm Bots](https://github.com/mahdymo/Tulkarm/blob/main/static/swarm_robots.gif)


This repository contains a simulation of swarm robots that communicate via MQTT and have real-time visualization using Matplotlib.

## How Swarm Robots Work

The swarm robot system simulates a set of robots that cooperate to achieve a common goal, such as navigating towards a target area, avoiding collisions, and maintaining cohesive movement as a group. Here's a breakdown of the key features and algorithms that govern the swarm behavior:

### 1. **Robot Communication via MQTT**
   - The robots communicate with each other using the **MQTT protocol**, a lightweight messaging protocol for small sensors and mobile devices. 
   - Each robot subscribes to a common MQTT topic (`swarm/coordinates`) where it shares its current position and listens for others' positions.
   - The MQTT broker (running on a Docker container) acts as the central hub for messaging between robots. 

### 2. **Robot Movement**
   Each robot calculates its movement based on the following basic principles:

   - **Cohesion**: Each robot tries to move towards the "center of the swarm," or the average position of all other robots. This helps the group stay together and move as a unit.
   - **Separation**: To avoid collisions, each robot also tries to move away from other nearby robots. This is done by calculating the distance to other robots, and if it's too close (e.g., within a certain threshold), the robot will move away to maintain a safe distance.
   - **Alignment**: The robots align their movement towards a common target. In this case, the robots have a target area (such as coordinates `[50, 50]`), and they update their velocity to move in that direction.

### 3. **Swarm Behavior Algorithm**
   The movement of the robots is influenced by the following forces:
   
   - **Cohesion**: This force pulls the robot towards the center of the swarm, ensuring that the robots remain together as a cohesive group.
   - **Separation**: This force pushes the robots away from each other if they are too close to one another, preventing collisions in tight spaces.
   - **Alignment**: This force adjusts the robot's velocity to steer it towards a common target area (for example, the `[50, 50]` target).

   The robots' final movement is determined by combining these forces into a single velocity vector, which is updated in real-time. The robots continuously adjust their position and velocity based on the information they receive from other robots in the swarm.

### 4. **Dynamic Target and Behavior Adaptation**
   While the robots are initially programmed to move towards a static target (e.g., coordinates `[50, 50]`), the target position can be dynamically updated during the simulation. This allows for more flexible and adaptive swarm behavior, such as:
   
   - **Moving to a new target area**: The target coordinates can be changed at any time, and the robots will adjust their movement accordingly to reach the new target.
   - **Avoiding dynamic obstacles**: Although not fully implemented in this version, future enhancements could include adding moving obstacles or dynamically changing environments that require robots to constantly adapt.

### 5. **Real-Time Visualization**
   - The robot positions are visualized in real-time using **Matplotlib**. The visualization shows the current positions of all robots as they move towards the target area.
   - The robot paths are updated on the plot every 0.1 seconds, providing a dynamic visual representation of the swarm's movement.

### 6. **Behavior and Coordination in the Swarm**
   - Each robot operates autonomously, but their behavior is coordinated through the shared MQTT topic. This decentralized control allows for a robust and scalable swarm system, where robots adjust their movements based on local information.
   - The swarm's behavior is emergent, meaning that the individual robot actions lead to complex group dynamics without the need for a central controller. The robots make decisions based on simple rules and the information they receive from nearby robots.

### 7. **Use of Docker Containers**
   - The entire system, including the MQTT broker, robots, and visualization, is containerized using **Docker**. This makes it easy to deploy and run the simulation on any system with Docker installed.
   - Each robot runs in its own container, and the robots communicate with each other via the MQTT broker, which is also containerized.



## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/username/Tulkarm.git
   cd Tulkarm
   docker-compose up --build

2. The robots will start communicating and moving in a swarm. The visualization will be shown in real-time.


## Visualization

The positions of the robots are visualized in real-time using Matplotlib. The robots move towards a common target area while avoiding collisions with each other.
`python3 visualizer.py`

##MQTT Broker

The robots communicate with each other via an MQTT broker running as part of the Docker setup. The messages are sent to a common topic, and each robot updates its position based on the swarm's state.

Yes, you can include a **Prerequisites** section in your `README.md` to ensure that users have the necessary tools and dependencies set up before running the swarm robot simulation. Here's an example of what you can add:

### **Prerequisites**

```markdown
## Prerequisites

Before running the swarm robots simulation, make sure you have the following installed on your system:

### 1. **Docker and Docker Compose**
   The simulation uses Docker to containerize the MQTT broker and the robot containers. You will need Docker and Docker Compose to build and run the containers.

   - **Install Docker**: Follow the official instructions for your platform:
     - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   
   - **Install Docker Compose**: Docker Compose is used to manage multi-container Docker applications.
     - [Install Docker Compose](https://docs.docker.com/compose/install/)

   After installing Docker and Docker Compose, you can verify the installation by running:

   ```bash
   docker --version
   docker-compose --version
   ```

### 2. **Python (for Robot Code Development)**
   While the robot containers are running inside Docker, you may choose to develop or test the robot logic locally. For that, you'll need **Python 3.9+** and the following libraries:

   - **Install Python 3**: Download and install Python from [python.org](https://www.python.org/).
   
   - **Install dependencies**: You can install the required Python libraries using `pip`. Run the following command to install the dependencies:

     ```bash
     pip install -r requirements.txt
     sudo apt-get update && sudo apt-get install -y python3-tk 
     ```
     

     **Dependencies** (included in `requirements.txt`):
     - `paho-mqtt`: For MQTT communication between robots.
     - `numpy`: For array and vector operations.
     - `matplotlib`: For real-time visualization.
     - `docker`: If you want to manage Docker containers via Python (optional).

### 3. **Git**
   Git is required to clone this repository to your local machine.

   - **Install Git**: Follow the instructions on the official Git website:
     - [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

   You can verify that Git is installed by running:

   ```bash
   git --version
   ```

### 4. **MQTT Broker (Optional if not using Docker)**
   The simulation uses the **Mosquitto MQTT broker** to facilitate communication between robots. You can either use the broker running in Docker (as part of the `docker-compose.yml` setup), or you can set up a local Mosquitto broker outside of Docker.

   If you're not using Docker, follow the official instructions to install Mosquitto:
   - [Mosquitto Installation Guide](https://mosquitto.org/download/)

### 5. **Matplotlib (For Visualization)**
   The robots' movement is visualized in real-time using **Matplotlib**. The visualization script requires the following libraries:

   - `matplotlib`: For plotting the robot positions.
   - `numpy`: For handling robot positions and vectors.

   You can install these dependencies by running:

   ```bash
   pip install matplotlib numpy
   ```

### 6. **Network Configuration (Optional)**
   If you're running the simulation on a cloud server or a remote machine, ensure the following:
   - Open port `1883` for MQTT communication.
   - Ensure that the MQTT broker and the robot containers are on the same network (this is automatically handled by Docker).


