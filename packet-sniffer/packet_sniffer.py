from scapy.all import sniff


def process_packet(packet):
    print(packet.summary())


print('[*] Starting packet capture...')

sniff(prn=process_packet, store=False)
