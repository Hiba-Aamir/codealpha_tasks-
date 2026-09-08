from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def analyze_packet(packet):

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        source_port = "-"
        destination_port = "-"

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"

        else:
            protocol = "Other"

        print("------------------------------")
        print("Source IP       :", source_ip)
        print("Destination IP  :", destination_ip)
        print("Protocol        :", protocol)
        print("Source Port     :", source_port)
        print("Destination Port:", destination_port)
        print("Packet Length   :", len(packet), "bytes")

        if Raw in packet:
            payload = packet[Raw].load
            print("Payload (Hex)   :", payload.hex()[:100])
        else:
            print("Payload         : No readable payload")


print("Starting Network Sniffer...")
print("Capturing 10 packets...\n")

sniff(count=10, prn=analyze_packet)

print("\nCapture completed.")
