import threading
from secure_socket import create_secure_server_socket
from event_processor import process_event
from performance import log_performance
from config import *
import sys, os

sys.path.append(os.path.abspath("../common"))
from protocol import decode_message

clients = []
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"✅ Connected: {addr}")

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            event = decode_message(data)
            processed = process_event(event)

            print(f"[{addr}] → {processed}")

            log_performance()

        except Exception as e:
            print(f"❌ Error with {addr}: {e}")
            break

    conn.close()
    print(f"🔴 Disconnected: {addr}")

def start_server():
    server = create_secure_server_socket(SERVER_IP, SERVER_PORT)

    print("🚀 Secure Server Running...")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
