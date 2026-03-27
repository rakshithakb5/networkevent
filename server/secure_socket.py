import ssl
import socket
import os

def create_secure_server_socket(ip, port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    cert_dir = os.path.join(os.path.dirname(__file__), '..', 'certs')
    cert_path = os.path.join(cert_dir, 'server.pem')
    key_path = os.path.join(cert_dir, 'server.key')
    context.load_cert_chain(cert_path, key_path)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(5)

    secure_sock = context.wrap_socket(sock, server_side=True)
    return secure_sock
