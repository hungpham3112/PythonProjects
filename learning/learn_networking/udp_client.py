import socket

server = ("127.0.0.1", 9001)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(1.0)
    s.sendto(b"hello", server)
    try:
        print(s.recvfrom(2048))
    except ConnectionRefusedError as e:
        print("no application reply:", type(e).__name__)
