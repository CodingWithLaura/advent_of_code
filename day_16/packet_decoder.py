def get_length_of_packet(packets_string, maximum):
    type_id = packets_string[3:6]
    length = 0
    if(type_id =='100'):   
        index = 6                       #<-- literal
        not_end = True
        while(not_end):
            is_end_null = packets_string[index]
            if(is_end_null == '0'):
                length = index + 5
                not_end = False
            else:
                index += 5
            if(index > maximum) and (maximum != -1): #nur Kontrolle
                length = 0
                not_end = False
    else:
        switch = packets_string[6]
        if(switch == '0'):  #length #pol
            length = int(packets_string[7:22],2) + 7 + 15
        else: #number  #pon
            number = int(packets_string[7:18],2)
            length = 18
            while(number>0):
                if(length + 7 > maximum) and (maximum != -1):
                    print("failure packet too short")
                    break
                actual_sub_packet_length = get_length_of_packet(packets_string[length:],-1)
                length += actual_sub_packet_length
                number -= 1   
    return length

def cut_sub_packets(packets_string, maximum, number = -1):
    packets = []
    start_index = 0
    length = 0
    actual_maximum = maximum
    not_end = True
    packet_count = 0
    while(not_end):  #packet für packet 
        length = get_length_of_packet(packets_string[start_index:], actual_maximum)
        packet = packets_string[start_index:(start_index+length)]
        packets.append(packet)
        packet_count += 1

        #swicth POL oder PON
        if(number == -1): #POL
            if(start_index+length > maximum-6):
                not_end = False
            else: #noch nicht am Ende
                start_index += length
                if(maximum != -1):
                    actual_maximum -= length
        else: #PON
            if(packet_count == number):
                break
            else:
                start_index += length
    return packets        

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

class Operator_packet_length_subs(Packet):  # <- schöni weil wir genau wissen wie groß paket mit seinen subpaketen ist
    def __init__(self,version, type_id, payload, sub_packet_list = []):
        super().__init__(version, type_id, payload) 
        self.sub_packet_list = sub_packet_list
        self.length = int(payload[1:16],2)
        sub_packets_payload = payload[16:(16 + self.length)]
        packets = cut_sub_packets(sub_packets_payload, self.length)
        for packet in packets:
             self.sub_packet_list.append(packet_factory(packet))  
        print("Operator_packet_length_subs")
    def set_sub_packets(self, sub_packet_list):
        return True
    
class Operator_packet_number_subs(Packet):   #<- unschöni, weil wir dynamisch durch das paket und seine subpakete durchhampeln müssen
    def __init__(self, version, type_id, payload, sub_packet_list = [] ):
        super().__init__(version, type_id, payload)
        self.sub_packet_list = sub_packet_list
        self.amount = int(payload[1:12],2)
        sub_packets_payload = payload[12:]
        packets = cut_sub_packets(sub_packets_payload, -1, self.amount)
        for packet in packets:
             self.sub_packet_list.append(packet_factory(packet))
        print("Operator_packet_number_subs")
    def set_sub_packets(self, sub_packet_list):
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
example2_bin = '0011100000000000011011 1101000101001010010001001000000000'
                                               # 00101001000100100
example3 = 'EE00D40C823060'
example3_bin = '11101110000000001101010000001100100000100011000001100000'

example4 = '8A004A801A8002F478'

example5 = '620080001611562C8802118E34'
example5_bin ='011 000 1 00000000010#000 000 0 000000000010110#000 100 0 1010#101 100 0 1011# 001 000 1 00000000010#000 100 0 1100#011 100 0 1101#00'
easy_example = '1a'

example6 ='C0015000016115A2E0802F182340'

example7 = 'A0016C880162017C3686B18A3D4780'

bin_list = hex_to_bin(example7)
print(bin_list)
my_packet = packet_factory(bin_list)
my_packet.print_summe()
