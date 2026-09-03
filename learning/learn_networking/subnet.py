from re import split


def network(ip) -> tuple[str, str, str]:
    ip, mask = ip.split("/")
    first, second, third, fourth = ip.split(".")
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(2**8 - 1)
    x = ~(1 << 32)

    # Ép kiểu sang 32-bit bằng cách AND với 0xFFFFFFFF
    print(f"{x & 0xFFFFFF00:032b}")
    print(f"{(0xFFFFFFFF << 8):024b}")
    # Output chuẩn C: 11111111011111111111111111111111


ip = "192.168.1.1/24"
print(network(ip))
