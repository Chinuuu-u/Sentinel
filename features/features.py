import pandas as pd 

flws = []

flow = {
    "SRC_IP":"",
    "DST_IP":"",
    "PROTOCOL":"",
    "Packets":"", 
    "Duration":"",
    "Packet/sec":"",
    "Byte/sec":"",
    "Avarage Packets Size":"",
    "Total Bytes":"",
    "Max Packet Size":"",
    "Min Packet Size":"",
                } 

def Features(flows):
    for key,val in flows.items():
                timestamps = [p["timestamp"] for p in val]
                duration = max(timestamps) - min(timestamps)
                total_bytes  = 0
                LgPacket = val[0]["size"]
                MinPacket = val[0]["size"]
                for p in val:
                    total_bytes += p["size"]
                    if LgPacket < p["size"]:
                        LgPacket = p["size"]
                    if MinPacket > p["size"]:
                        MinPacket = p["size"]
                
                
                if duration > 0:
                    p_sec = len(val) / duration
                    b_sec = total_bytes / duration
                else:
                    p_sec = 0
                    b_sec = 0
                    
     
                # print("SRC_IP:",key[0],key[2])
                # print("DST_IP:",key[1],key[3])
                # print("PROTOCOL:",key[4])
                # print("Packets:", len(val))
                # print("Duration:",duration)
                # print("Packet/sec:", p_sec)
                # print("Byte/sec:", b_sec)
                # print("Avarage Packets Size:",total_bytes /len(val))
                # print("Total Bytes:",total_bytes )
                # print("Max Packet Size",LgPacket)
                # print("Min Packet Size",MinPacket)
                
                
                flow = {
                            "SRC_IP": key[0],
                            "DST_IP": key[1],
                            "SRC_PORT": key[2],
                            "DST_PORT": key[3],
                            "PROTOCOL": key[4],

                            "Packets": len(val),
                            "Duration": duration,

                            "Packet/sec": p_sec,
                            "Byte/sec": b_sec,

                            "Average Packet Size": total_bytes /len(val),
                            "Total Bytes": total_bytes,

                            "Max Packet Size": LgPacket,
                            "Min Packet Size": MinPacket,
                        }

                flws.append(flow)
                
               
                
                
                # for p in val:
                #     print("         ",p["src_ip"],p["src_port"],"-->",p["dst_ip"],p["dst_port"],p["size"])
    
                # print("")
    f = pd.DataFrame(flws)
    f.to_csv("data.csv",index=False)               