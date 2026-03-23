import ssl
import socket

def create_secure_server_socket(ip, port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("../certs/server.pem", "../certs/server.key")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(5)

    secure_sock = context.wrap_socket(sock, server_side=True)
    return secure_sock