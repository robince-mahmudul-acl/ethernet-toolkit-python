"""
Author: Mahmudul Islam (Robince)
Email: [mahmudulislam299@gmail.com
"""


import time
from scapy.all import Ether, sendp

def send_ethernet_frame(interface, dest_mac, src_mac):
    a = 1  # Initialize the variable
    
    while True:
        # Create the payload with the incrementing variable
        payload = f'Hello packet Payload number: {a}'.encode('utf-8')

        # Build Ethernet frame
        frame = Ether(dst=dest_mac, src=src_mac) / payload

        # Send Ethernet frame
        sendp(frame, iface=interface)
        print(f"Sent Ethernet frame on {interface} with payload: {payload.decode('utf-8')}")

        # Increment the variable
        a += 1

        # Wait for 2 seconds before sending the next frame
        time.sleep(2)

if __name__ == "__main__":
    interface = 'Ethernet 2'  # Change this to your Ethernet 2 adapter name
    dest_mac = '00:E0:4C:36:5E:CE'  # MAC address of Ethernet 3

    # dest_mac = 'AA:BB:CC:DD:EE:FF' # switch mac address
    # dest_mac = 'AA:BB:CC:DD:EE:FF'  # MAC address of Ethernet 3
    src_mac = '00:E0:4C:68:18:15'  # MAC address of Ethernet 2

    send_ethernet_frame(interface, dest_mac, src_mac)
