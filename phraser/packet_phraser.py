from scapy.all import rdpcap, IP, TCP, UDP



packet_records  = []
packets = rdpcap("C:\\Users\\Chirag\\Desktop\\Sentinal\\data\\raw\\data.pcapng")

def Phraser():

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
        
        packet_records.append({
        "src_ip": data.src,
        "dst_ip": data.dst,
        "src_port": SPORT,
        "dst_port": DPORT,
        "protocol": PROTOCOL,
        "size": len(packet),
        "timestamp": float(packet.time)
    })
    return packet_records
    