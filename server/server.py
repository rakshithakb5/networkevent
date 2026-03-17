import socket
from config import *
from event_processor import process_event, filter_event
import sys
import os

# Import common module
sys.path.append(os.path.abspath("../common"))
from event_format import deserialize_event

clients = set()
event_stats = {
    "CRITICAL": 0,
    "WARNING": 0,
    "NORMAL": 0
}

def print_dashboard():
    print("\n========== NETWORK DASHBOARD ==========")
    print(f"Connected Clients: {len(clients)}")
    print(f"CRITICAL: {event_stats['CRITICAL']}")
    print(f"WARNING : {event_stats['WARNING']}")
    print(f"NORMAL  : {event_stats['NORMAL']}")
    print("======================================\n")

def print_event(event, addr):
    print(f"[{event['timestamp']}] {addr}")
    print(f"Node: {event['node_id']}")
    print(f"Type: {event['type']} → {event['class']}")
    print(f"Message: {event['message']}")
    print("--------------------------------------")

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))

    print(f"🚀 Server running on {SERVER_IP}:{SERVER_PORT}")

    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)

        try:
            event = deserialize_event(data)

            # Register client
            clients.add(addr)

            # Filter
            if not filter_event(event):
                continue

            # Process
            event = process_event(event)

            # Update stats
            event_stats[event["class"]] += 1

            # Display
            print_event(event, addr)
            print_dashboard()

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    start_server()