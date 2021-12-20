def  cut_sub_packets(packets_string, maximum):
    packets = []
    not_end = True
    start_index = 0
    index = 6
    print(packets_string)
    while(not_end):
        is_end_null = packets_string[index]
        if(is_end_null == '0'):
            packet = packets_string[start_index:(index+4)]
            print(packet)
            packets.append(packet)
            start_index = index + 5
            index = start_index + 6
        else:
            index += 5
        print(start_index)    
        print(index)    
        if(index >= maximum):
            not_end = False
    return packets        
# v              
# 111 100 1 0001 1 1101 0 1001 # 110 100 ..
class Packet:
    summe = 0
    def __init__(self, version, type_id, payload):
        self.version = version
        self.type_id = type_id
        self.payload = payload
        Packet.summe += int(version, 2)
        print("Packet")
    def set_sub_packets(self,sub_packet_list):
        return False
    def print_summe(self):
        print(Packet.summe)

class Literal_packet(Packet):
    def __init__(self, version, type_id, payload):
        super().__init__(version, type_id, payload)
        print("Literal_packet")
    def set_sub_packets(sub_packet_list):
        return False


class Operator_packet_length_subs(Packet):
    def __init__(self,version, type_id, payload, sub_packet_list = []):
        super().__init__(version, type_id, payload) 
        self.sub_packet_list = sub_packet_list
        self.length = int(payload[1:16],2)
        sub_packets_payload = payload[16:(16 + self.length)]
        packets = cut_sub_packets(sub_packets_payload, self.length)
        for packet in packets:
             self.sub_packet_list.append(packet_factory(packet))  
        print("Operator_packet_length_subs")
    def set_sub_packets(sub_packet_list):
        return True
    
class Operator_packet_number_subs(Packet):
    def __init__(self, version, type_id, payload, sub_packet_list = [] ):
        super().__init__(version, type_id, payload)
        self.sub_packet_list = sub_packet_list
        self.amount = int(payload[1:12],2)
        print("Operator_packet_number_subs")
    def set_sub_packets(sub_packet_list):
        return True    

def packet_factory(bin_list):
    version = bin_list[:3]
    type_id = bin_list[3:6]
    print(version)
    print(type_id)
    payload = bin_list[6:]
    
    if(type_id == "100"):
        literal = Literal_packet(version,type_id,payload)   
        return literal
    else: # operator packet
        switch = bin_list[6:7]
        if(switch == '0'): # length
            operator_packet = Operator_packet_length_subs(version,type_id,payload)
        else: # number
            operator_packet = Operator_packet_number_subs(version,type_id,payload)
        return operator_packet
def hex_to_bin(hexadecimal_string):
    char_list = list(hexadecimal_string)
    bin_list = []
    scale = 16
    for item in char_list:
        bin_item = "{0:04b}".format(int(item, scale))
        bin_list.append(bin_item)
    return ''.join(bin_list)


example1 = "D2FE28"
example1_bin = 110100101111111000101000

example2 = '38006F45291200'

example3 = 'EE00D40C823060'

easy_example = '1a'
bin_list = hex_to_bin(example2)
print(bin_list)
my_packet = packet_factory(bin_list)
my_packet.print_summe()
