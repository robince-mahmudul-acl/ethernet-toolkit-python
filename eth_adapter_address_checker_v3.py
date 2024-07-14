"""
Author: Mahmudul Islam (Robince)
Email: [mahmudulislam299@gmail.com
"""

import psutil

def get_ethernet_adapters_info():
    # Get all network interfaces
    network_interfaces = psutil.net_if_addrs()
    network_stats = psutil.net_if_stats()
    
    # Iterate through the interfaces and filter out Ethernet adapters
    ethernet_adapters_info = []
    for interface_name, interface_addresses in network_interfaces.items():
        for address in interface_addresses:
            if address.family == psutil.AF_LINK:  # This checks for MAC addresses, typical of Ethernet
                # Additional check to ensure it's an Ethernet adapter
                if interface_name.lower().startswith(('eth', 'en', 'ethernet', 'lan')):
                    adapter_info = {
                        'name': interface_name,
                        'mac_address': address.address,
                        'is_up': network_stats[interface_name].isup,
                        'speed': network_stats[interface_name].speed
                    }
                    ethernet_adapters_info.append(adapter_info)
                    break
    
    return ethernet_adapters_info

if __name__ == "__main__":
    adapters_info = get_ethernet_adapters_info()
    if adapters_info:
        print("Ethernet adapters found:")
        for adapter in adapters_info:
            print(f"Name: {adapter['name']}")
            print(f"MAC Address: {adapter['mac_address']}")
            print(f"Is Up: {'Yes' if adapter['is_up'] else 'No'}")
            print(f"Speed: {adapter['speed']} Mbps")
            print()
    else:
        print("No Ethernet adapters found.")
