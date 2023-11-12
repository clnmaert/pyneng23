import subprocess


def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(['192.168.74.1', '127.0.0.1', 'ya.ru', '192.168.12.1' '192.168.11.1']))