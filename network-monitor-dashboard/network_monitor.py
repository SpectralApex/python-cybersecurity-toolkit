import psutil
import time


def monitor_network():
    old_data = psutil.net_io_counters()

    while True:
        time.sleep(1)
        new_data = psutil.net_io_counters()

        bytes_sent = new_data.bytes_sent - old_data.bytes_sent
        bytes_recv = new_data.bytes_recv - old_data.bytes_recv

        print(f'Upload: {bytes_sent / 1024:.2f} KB/s | Download: {bytes_recv / 1024:.2f} KB/s')

        old_data = new_data


if __name__ == '__main__':
    print('[*] Starting Network Monitor...')
    monitor_network()
