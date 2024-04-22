import os
import random
import string
from scapy.all import *

#A simple Pcap file generator with random String in it

file_num = 37

def generate_flag():
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return f"Flag{{{random_string}}}"

def generate_random_packet():
    protocol = random.choice([TCP, UDP, ICMP, DNS])
    packet = IP(src=".".join(map(str, (random.randint(0, 255) for _ in range(4)))), 
                dst=".".join(map(str, (random.randint(0, 255) for _ in range(4))))) / protocol()
    return packet

def generate_pcap_with_flag(filename):
    packet_count = random.randint(100, 200)
    packets = []
    for _ in range(packet_count - 1):
        packet = generate_random_packet()
        packets.append(packet)
    flag_packet = generate_random_packet() / generate_flag()
    packets.append(flag_packet)
    random.shuffle(packets)
    wrpcap(filename, packets)

def main():
    if not os.path.exists("pcap_files"):
        os.makedirs("pcap_files")
    #
    for i in range(file_num):
        filename = f"pcap_files/file_{i}.pcap"
        generate_pcap_with_flag(filename)
    print("Random pcap files generated successfully.")

if __name__ == "__main__":
    main()
