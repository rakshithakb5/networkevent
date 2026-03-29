import time
import random
import argparse
from secure_socket import create_secure_client_socket
import sys, os

# Add common module to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'common'))
from protocol import encode_message

SERVER_IP = "SERVER_IP"
SERVER_PORT = 9999

events = [
    {"type": "FAILURE", "msg": "Node down"},
    {"type": "THRESHOLD", "msg": "CPU high"},
    {"type": "INFO", "msg": "OK"}
]

def start_client():
    parser = argparse.ArgumentParser(description="Network event client")
    parser.add_argument("--ip", default=SERVER_IP, help="Server IP")
    parser.add_argument("--port", type=int, default=SERVER_PORT, help="Server port")
    parser.add_argument("--interval", type=float, default=2.0, help="Seconds between events")
    parser.add_argument("--count", type=int, default=0, help="Total events to send (0 = infinite)")
    args = parser.parse_args()

    try:
        sock = create_secure_client_socket(args.ip, args.port)
    except ConnectionRefusedError:
        print(f"Server {args.ip}:{args.port} is unreachable/offline. Exiting...")
        return
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return

    sent = 0
    started = time.time()

    try:
        while args.count == 0 or sent < args.count:
            event = random.choice(events)

            sock.sendall(encode_message(event))
            print("Sent:", event)
            sent += 1

            time.sleep(max(0.0, args.interval))
    except (ConnectionRefusedError, ConnectionResetError, BrokenPipeError, ConnectionAbortedError) as e:
        print(f"\nConnection lost or server disconnected abruptly: {e}")
    except Exception as e:
        print(f"\nAn error occurred during transmission: {e}")
    finally:
        sock.close()

    elapsed = max(0.001, time.time() - started)
    print(f"\nSummary: sent={sent}, duration={elapsed:.2f}s, rate={sent/elapsed:.2f} events/sec")

if __name__ == "__main__":
    start_client()
