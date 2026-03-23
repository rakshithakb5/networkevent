import time
import random
from secure_socket import create_secure_client_socket
import sys, os

sys.path.append(os.path.abspath("../common"))
from protocol import encode_message

SERVER_IP = "127.0.0.1"
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