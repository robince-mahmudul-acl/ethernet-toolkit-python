# Ethernet Address Checker v3, Ether Packet Sender, and Ethernet Packet Receiver

This repository contains Python scripts for checking Ethernet MAC addresses, sending Ethernet packets, and receiving Ethernet packets using the `scapy` library. These scripts are useful for network testing, debugging, and custom Ethernet packet transmission.

## Contents

- `eth_address_checker_v3.py`: Checks and validates Ethernet addresses of adapter.
- `eth_packet_sender.py`: Constructs and sends Ethernet packets to a specified destination.
- `eth_packet_receiver.py`: Listens for and receives Ethernet packets.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed via `pip`):
  - `scapy` (for packet crafting and network analysis)
  - `netifaces` (for network interface information)


### Usage

#### Ethernet Address Checker

To check and validate Ethernet addresses, run:
```bash
python eth_adapter_address_checker_v3.py
```
