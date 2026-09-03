import socket

addr = ("127.0.0.1", 9001)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(addr)
    data, peer = s.recvfrom(2048)
    print(data, peer)
    s.sendto(b"echo: " + data, peer)
