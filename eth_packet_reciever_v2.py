"""
Author: Mahmudul Islam (Robince)
Email: [mahmudulislam299@gmail.com
"""

from scapy.all import sniff, Ether

# Define the source MAC address to filter
# source_mac = "00:E0:4C:68:18:15"
# source_mac ='00:E0:4C:36:5E:CE'

source_mac = "00:e0:4c:68:18:15"

def handle_packet(packet):
    if packet.haslayer(Ether):
        eth = packet.getlayer(Ether)
        # if eth.src == source_mac:  # Check if the source MAC address matches
        print("Received Ethernet frame:")
        print(f"Source MAC: {eth.src}")
        print(f"Destination MAC: {eth.dst}")
        print(f"EtherType: {eth.type}")
        if eth.payload:
            print(f"Payload: {bytes(eth.payload).decode('utf-8', errors='ignore')}")
        print("\n\n")

def receive_ethernet_frame(interface):
    print(f"Listening for Ethernet frames on {interface}")
    sniff(iface=interface, prn=handle_packet, store=0)

if __name__ == "__main__":
    interface = 'Ethernet 3'  # Change this to your Ethernet 3 adapter name
    
    receive_ethernet_frame(interface)
