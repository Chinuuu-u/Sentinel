from datetime import datetime
from collections import defaultdict


flows = defaultdict(list)


def FlowBuilder(packet_records):
    for packet in packet_records:
        flow_key = (
                packet["src_ip"],
                packet["dst_ip"],
                packet["src_port"],
                packet["dst_port"],
                packet["protocol"],
                )
        flows[flow_key].append(packet)
    return flows    
        