from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from utils import protocol_name, format_payload

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        proto = protocol_name(ip_layer.proto)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        print("=" * 60)
        print(f"Protocol:       {proto}")
        print(f"Source IP:      {src_ip}")
        print(f"Destination IP: {dst_ip}")
        # Extract payload data, decode safely
        if Raw in packet:
            payload = format_payload(bytes(packet[Raw].load))
            print(f"Payload:        {payload}")
        else:
            print("Payload:        [No Data]")
        print("=" * 60)

def start_sniffing(interface=None, packet_filter="ip"):
    print("Starting packet capture. Press CTRL+C to stop.")
    sniff(prn=packet_callback, filter=packet_filter, iface=interface, store=0)
