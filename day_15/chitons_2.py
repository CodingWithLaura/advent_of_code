def get_path(costs_dict,start,end):
    path = [end]
    node = end
    while(node != start):
        vorgaenger = costs_dict[node][1]
        path.append(vorgaenger)
        node = vorgaenger
    return path 

def next_minimal_node(costs_dict, visited_nodes):
    # minimum
    candidate = (-1,-1)
    actual_minimum = -1
    for key in costs_dict:
        value = costs_dict[key][0]
        if(value != -1):
            if (actual_minimum == -1) and (not key in visited_nodes):
                actual_minimum = value
                candidate = key
            elif (actual_minimum > value) and (not key in visited_nodes):
                actual_minimum = value
                candidate = key
    return candidate        

def find_path(graph_dict, start, end):
    # initialisierung
    unvisited_nodes = set()
    costs_dict = dict()
    for key_node in graph_dict:
        unvisited_nodes.add(key_node)
        costs_dict[key_node] = (-1,(-1,-1)) 
    costs_dict[(0,0)] = (0,(0,0))
    visited_nodes = set()
    node = start
    not_abbruch = True
    marker = 0
    while(not_abbruch):
        cost = costs_dict[node][0] 
        neighbor_werte = graph_dict[node]
        neighbors = set()
        for neighbor in neighbor_werte:
            distance = graph_dict[node][neighbor]
            start_to_neighbor_cost = distance + cost
            if costs_dict[neighbor][0] == -1:
                costs_dict[neighbor] = (start_to_neighbor_cost,node)
            elif costs_dict[neighbor][0] > start_to_neighbor_cost:
                costs_dict[neighbor] = (start_to_neighbor_cost,node)
        visited_nodes.add(node)
        node = next_minimal_node(costs_dict, visited_nodes)
        if(node == (-1,-1)):
            not_abbruch = False
        marker +=1
        if(marker %1000) == 0:
            print(marker)
    return [ costs_dict[end][1]], costs_dict[end][0],costs_dict

data = []

f = open("real_numbers.txt", "r")
lines = f.readlines()
for x in lines:
    data.append(list(map(int,x.rstrip("\n"))))

#data -> data_advanced
size_x = len(data[0]) #3
size_y = len(data)    #3

advance_scale = 5
data_advanced = [[0]*size_x*advance_scale for i in range(size_y*advance_scale)]

offset_y = -1
for y_index in range(advance_scale*size_y):
    offset_x = -1
    if(y_index % size_y) == 0:
        offset_y +=1
    for x_index in range(advance_scale*size_x):
        if(x_index % size_x) == 0:
            offset_x +=1
        wert_raw = data[y_index % size_y][x_index % size_x] + offset_y + offset_x    
        data_advanced[y_index][x_index] = ((wert_raw-1)%9)+1

my_dict = dict()

# data-matrix zu graph (dictionary)
for y_index in range(len(data_advanced)):
    for x_index in range(len(data_advanced[y_index])-1):
        node1 = (x_index, y_index)
        node2 = (x_index+1, y_index)
        wert_r_l = data_advanced[y_index][x_index+1]
        wert_l_r = data_advanced[y_index][x_index]
        # my_dict[node1] = {node2:wert}
        if node1 in my_dict:
            edge_n1_n2 = my_dict[node1]
            edge_n1_n2[node2] = wert_r_l
        else:    
            edge_n1_n2 = dict()
            edge_n1_n2[node2] = wert_r_l
            my_dict[node1] = edge_n1_n2
        
        # my_dict[node2] = {node1:wert}
        if node2 in my_dict:
            edge_n2_n1 = my_dict[node2]
            edge_n2_n1[node1] = wert_l_r
        else:
            edge_n2_n1 = dict()
            edge_n2_n1[node1] = wert_l_r
            my_dict[node2] = edge_n2_n1

for x_index in range(len(data_advanced[0])):
    for y_index in range(len(data_advanced)-1):
        node1 = (x_index, y_index)
        node2 = (x_index, y_index+1)
        wert_o_u = data_advanced[y_index+1][x_index]
        wert_u_o = data_advanced[y_index][x_index]
        
        # my_dict[node1] = {node2:wert}
        if node1 in my_dict:
            edge_n1_n2 = my_dict[node1]
            edge_n1_n2[node2] = wert_o_u
        else:    
            edge_n1_n2 = dict()
            edge_n1_n2[node2] = wert_o_u
            my_dict[node1] = edge_n1_n2
        
        # my_dict[node2] = {node1:wert}
        if node2 in my_dict:
            edge_n2_n1 = my_dict[node2]
            edge_n2_n1[node1] = wert_u_o
        else:
            edge_n2_n1 = dict()
            edge_n2_n1[node1] = wert_u_o
            my_dict[node2] = edge_n2_n1

path_list = []
start = (0,0)
end = (len(data_advanced[0])-1,len(data_advanced)-1 )
path_list, risk, c_d = find_path(my_dict, start, end)
print(path_list)
print(risk)
path = get_path(c_d,start,end)
reverse_path = path.copy()
reverse_path.reverse()
print(reverse_path)

summe = 0
lastnode = (0,0)
for item in reverse_path:
    x = item[0]
    y = item[1]
    node = (x,y)
    value = data_advanced[y][x]
    if(x ==0 and y == 0):
        summe += 0
    else:    
        summe += value 
        edge = my_dict[lastnode][node]
        equal = (edge == value)
        print("{} {} {} {} {}".format(lastnode, node, edge, value, equal))
    lastnode = node
print(summe)    
