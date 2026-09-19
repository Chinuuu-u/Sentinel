from scapy.all import rdpcap, IP, TCP, UDP
from datetime import datetime
packets = rdpcap("C:\\Users\\Chirag\\Desktop\\SenetryFlow\\data\\data.pcapng")

TupeObj = []

for packet in packets:
    
    if IP not in packet:
        continue
    if TCP in packet:
        PROTOCOL = "TCP"
        SPORT = packet[TCP].sport
        DPORT = packet[TCP].dport
    elif UDP in packet:
        PROTOCOL = "UDP"
        SPORT = packet[UDP].sport
        DPORT = packet[UDP].dport
    else:
        PROTOCOL = "OTHER"
        SPORT = None
        DPORT = None 
    
    data = packet[IP]
    time = (datetime.fromtimestamp(float(packet.time))) 
    
    TupeObj.append({
    "src_ip": data.src,
    "dst_ip": data.dst,
    "src_port": SPORT,
    "dst_port": DPORT,
    "protocol": PROTOCOL,
    "size": len(packet),
    "timestamp": time
})

for info in TupeObj:
    print(info)