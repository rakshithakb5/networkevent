import threading
import time
import ssl
from secure_socket import create_secure_server_socket
from event_processor import process_event
from performance import (
    log_performance,
    log_malformed,
    log_disconnect,
    log_ssl_error,
)
from config import *
import sys, os

# Add common module to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'common'))
from protocol import decode_message

clients = []
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"✅ Connected: {addr}")

    while True:
        try:
            started = time.perf_counter()
            data = conn.recv(1024)

            if not data:
                log_disconnect()
                break

            try:
                event = decode_message(data)
            except Exception as e:
                log_malformed()
                print(f"⚠️ Invalid payload from {addr}: {e}")
                continue

            processed = process_event(event)

            print(f"[{addr}] → {processed}")

            latency_ms = (time.perf_counter() - started) * 1000
            log_performance(latency_ms)

        except ssl.SSLError as e:
            log_ssl_error()
            print(f"❌ SSL error with {addr}: {e}")
            break

        except (ConnectionResetError, BrokenPipeError, OSError) as e:
            log_disconnect()
            print(f"❌ Connection error with {addr}: {e}")
            break

        except Exception as e:
            print(f"❌ Error with {addr}: {e}")
            break

    conn.close()
    print(f"🔴 Disconnected: {addr}")

def start_server():
    server = create_secure_server_socket(SERVER_IP, SERVER_PORT)

    print("🚀 Secure Server Running...")

    while True:
        try:
            conn, addr = server.accept()

            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
        except ssl.SSLError as e:
            print(f"⚠️ SSL Handshake failed during accept: {e}")
        except Exception as e:
            print(f"⚠️ Error accepting connection: {e}")

if __name__ == "__main__":
    start_server()
