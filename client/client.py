import time
import random
from secure_socket import create_secure_client_socket
import sys, os

# Add common module to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'common'))
from protocol import encode_message

SERVER_IP = "INSERT_IP"
SERVER_PORT = 9999

events = [
    {"type": "FAILURE", "msg": "Node down"},
    {"type": "THRESHOLD", "msg": "CPU high"},
    {"type": "INFO", "msg": "OK"}
]

def start_client():
    sock = create_secure_client_socket(SERVER_IP, SERVER_PORT)

    while True:
        event = random.choice(events)

        sock.send(encode_message(event))
        print("Sent:", event)

        time.sleep(2)

if __name__ == "__main__":
    start_client()
