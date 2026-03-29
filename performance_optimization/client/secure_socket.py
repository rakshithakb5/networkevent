import ssl
import socket

def create_secure_client_socket(ip, port):
    context = ssl.create_default_context()
    # Disable certificate verification for self-signed certificates (testing only)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(sock, server_hostname=ip)

    secure_sock.connect((ip, port))
    return secure_sock
