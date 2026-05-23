import socket
from colorama import Fore, init

init(autoreset=True)

COMMON_PORTS = [
    20, 21, 22, 23, 25, 53, 80,
    110, 135, 139, 143, 443, 445,
    3306, 3389, 8080
]


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port}")
        else:
            print(Fore.RED + f"[CLOSED] Port {port}")

        sock.close()

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nScan interrupted.")
        exit()

    except socket.gaierror:
        print(Fore.RED + "Hostname could not be resolved.")
        exit()

    except socket.error:
        print(Fore.RED + "Server not responding.")
        exit()


def main():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "     Basic Python Port Scanner")
    print(Fore.CYAN + "=" * 50)

    target = input("Enter target IP or hostname: ")

    print(Fore.YELLOW + f"\nScanning target: {target}\n")

    for port in COMMON_PORTS:
        scan_port(target, port)


if __name__ == "__main__":
    main()
