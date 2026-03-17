import socket
import time
import random
import sys
import os

# Import common module
sys.path.append(os.path.abspath("../common"))
from event_format import create_event, serialize_event

SERVER_IP = "192.168.1.33"   # 🔥 CHANGE THIS
SERVER_PORT = 9999

NODE_ID = f"node-{random.randint(1000,9999)}"

events = [
    ("FAILURE", "Node crashed"),
    ("THRESHOLD", "CPU usage high"),
    ("THRESHOLD", "Memory usage high"),
    ("INFO", "Heartbeat OK"),
    ("DEBUG", "Temp log")
]

def send_events():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Client started → {NODE_ID}")

    while True:
        event_type, message = random.choice(events)

        event = create_event(event_type, message, NODE_ID)

        # Simulate packet loss (20%)
        if random.random() < 0.2:
            print("⚠️ Packet dropped (simulated)")
            time.sleep(1)
            continue

        sock.sendto(serialize_event(event), (SERVER_IP, SERVER_PORT))

        print(f"Sent: {event}")
        time.sleep(2)

if __name__ == "__main__":
    send_events()