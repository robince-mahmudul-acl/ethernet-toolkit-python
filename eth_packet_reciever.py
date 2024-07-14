"""
Author: Mahmudul Islam (Robince)
Email: [mahmudulislam299@gmail.com
"""

from scapy.all import sniff, Ether

def handle_packet(packet):
    if packet.haslayer(Ether):
        eth = packet.getlayer(Ether)
        print(f"Received Ethernet frame:")
        print(f"Source MAC: {eth.src}")
        print(f"Destination MAC: {eth.dst}")
        print(f"EtherType: {eth.type}")
        if eth.payload:
            print(f"Payload: {bytes(eth.payload).decode('utf-8', errors='ignore')}")
        print(f"\n\n")

def receive_ethernet_frame(interface):
    print(f"Listening for Ethernet frames on {interface}")
    sniff(iface=interface, prn=handle_packet, store=0)

if __name__ == "__main__":
    interface = 'Ethernet 3'  # Change this to your Ethernet 3 adapter name
    
    receive_ethernet_frame(interface)
