from flow.flow_builder import FlowBuilder
from features.features import Features
from phraser.packet_phraser import Phraser
def main():
    packet_rec = Phraser();
    flows = FlowBuilder(packet_records=packet_rec)
    Features(flows=flows)
    
    

if __name__=='__main__':
    main()