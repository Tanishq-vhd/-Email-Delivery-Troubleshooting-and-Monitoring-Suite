import ssl
import socket

def check_tls_cert(hostname, port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print("Cipher:", ssock.cipher())
                print("TLS version:", ssock.version())
                print("Certificate:", ssock.getpeercert())
    except Exception as e:
        print("TLS Check Failed:", e)
