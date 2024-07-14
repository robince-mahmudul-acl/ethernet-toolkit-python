"""
Author: Mahmudul Islam (Robince)
Email: [mahmudulislam299@gmail.com
"""

import psutil

def get_ethernet_adapters():
    # Get all network interfaces
    network_interfaces = psutil.net_if_addrs()
    
    # Iterate through the interfaces and filter out Ethernet adapters
    ethernet_adapters = []
    for interface_name, interface_addresses in network_interfaces.items():
        for address in interface_addresses:
            if address.family == psutil.AF_LINK:  # This checks for MAC addresses, typical of Ethernet
                ethernet_adapters.append(interface_name)
                break
    
    return ethernet_adapters

if __name__ == "__main__":
    adapters = get_ethernet_adapters()
    if adapters:
        print("Ethernet adapters found:")
        for adapter in adapters:
            print(f"- {adapter}")
    else:
        print("No Ethernet adapters found.")
