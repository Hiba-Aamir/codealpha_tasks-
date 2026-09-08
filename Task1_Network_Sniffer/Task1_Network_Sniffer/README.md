
# Task 1: Basic Network Sniffer

## Objective

The objective of this task is to build a basic network sniffer in Python that captures and analyzes network packets using the Scapy library.

The program displays useful packet information such as:

* Source IP address
* Destination IP address
* Protocol
* Source port
* Destination port
* Packet length
* Payload in hexadecimal format

## Technologies Used

* Python
* Scapy
* Npcap
* Windows

## Features

* Captures network packets in real time
* Identifies IPv4 packets
* Detects TCP, UDP, and ICMP protocols
* Displays source and destination IP addresses
* Displays source and destination ports
* Displays packet length
* Displays available payload data in hexadecimal format

## How It Works

The program uses Scapy's `sniff()` function to capture network packets.

For each captured packet, the program checks whether it contains an IP layer. It then identifies the transport protocol and extracts the relevant information.

### Packet Flow

```text
Network Traffic
       ↓
Packet Capture
       ↓
Packet Analysis
       ↓
Display Information
```

## Sample Output

```text
------------------------------
Source IP       : 192.168.1.109
Destination IP  : 150.171.109.163
Protocol        : TCP
Source Port     : 60753
Destination Port: 443
Packet Length   : 55 bytes
Payload (Hex)   : 00
```

Another example:

```text
------------------------------
Source IP       : 192.168.1.109
Destination IP  : 103.11.1.110
Protocol        : UDP
Source Port     : 53410
Destination Port: 443
Packet Length   : 1250 bytes
Payload (Hex)   : 5a975640e7a4...
```

## Packet Analysis

The captured packets demonstrated both TCP and UDP traffic.

TCP traffic was observed using destination port 443, which is commonly associated with HTTPS/TLS traffic.

UDP traffic was also observed on port 443. Modern protocols such as QUIC/HTTP/3 can use UDP port 443.

Some payloads appeared as hexadecimal or unreadable binary data because network application traffic can be encrypted or represented as binary data.



First, install Scapy:

```bash
pip install scapy
```

Then run the program:

```bash
python sniffer.py
```

The program captures 10 packets and displays their information in the terminal.



Through this task, I learned how network packets are captured and analyzed using Python and Scapy.

I learned how to identify:

* Source and destination IP addresses
* Network protocols
* Source and destination ports
* Packet sizes
* Payload data

This task also helped me understand the basic flow of data through a network and the difference between TCP and UDP traffic.

 Conclusion

The Basic Network Sniffer successfully captures and analyzes network traffic packets.

It provides fundamental packet-level information that can be useful for learning network protocols and basic network security analysis.
