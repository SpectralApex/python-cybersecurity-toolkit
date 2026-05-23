import socket
import threading
import argparse
from queue import Queue
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

queue = Queue()
open_ports = []


def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "      Advanced Python Port Scanner")
    print(Fore.CYAN + "=" * 60)



def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            try:
                banner_data = sock.recv(1024).decode().strip()
            except:
                banner_data = "No banner"

            print(Fore.GREEN + f"[OPEN] Port {port} | Service: {service} | Banner: {banner_data}")
            open_ports.append(port)

        sock.close()

    except:
        pass



def worker(target):
    while not queue.empty():
        port = queue.get()
        scan_port(target, port)
        queue.task_done()



def main():
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")

    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-th", "--threads", type=int, default=100, help="Number of threads")

    args = parser.parse_args()

    banner()

    print(Fore.YELLOW + f"Target: {args.target}")
    print(Fore.YELLOW + f"Port Range: {args.start}-{args.end}")
    print(Fore.YELLOW + f"Threads: {args.threads}\n")

    start_time = datetime.now()

    for port in range(args.start, args.end + 1):
        queue.put(port)

    for _ in range(args.threads):
        thread = threading.Thread(target=worker, args=(args.target,))
        thread.daemon = True
        thread.start()

    queue.join()

    end_time = datetime.now()
    duration = end_time - start_time

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.CYAN + f"Scan completed in: {duration}")
    print(Fore.CYAN + f"Open Ports Found: {len(open_ports)}")
    print(Fore.CYAN + "=" * 60)


if __name__ == "__main__":
    main()
