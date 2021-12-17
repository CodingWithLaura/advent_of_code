def next_minimal_node(cost_dict, visited_nodes):
    # minimum
    candidate = (-1,-1)
    actual_minimum = -1
    for key in cost_dict:
        value = cost_dict[key][0]
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
    return [ costs_dict[end][1]], costs_dict[end][0]

data = []

f = open("real_numbers.txt", "r")
lines = f.readlines()
for x in lines:
    data.append(list(map(int,x.rstrip("\n"))))

my_dict = dict()

for y_index in range(len(data)):
    for x_index in range(len(data[y_index])-1):
        node1 = (x_index, y_index)
        node2 = (x_index+1, y_index)
        wert = data[y_index][x_index+1]

        # my_dict[node1] = {node2:wert}
        if node1 in my_dict:
            edge_n1_n2 = my_dict[node1]
            edge_n1_n2[node2] = wert
        else:    
            edge_n1_n2 = dict()
            edge_n1_n2[node2] = wert
            my_dict[node1] = edge_n1_n2
        
        # my_dict[node2] = {node1:wert}
        if node2 in my_dict:
            edge_n2_n1 = my_dict[node2]
            edge_n2_n1[node1] = wert
        else:
            edge_n2_n1 = dict()
            edge_n2_n1[node1] = wert
            my_dict[node2] = edge_n2_n1

for x_index in range(len(data[0])):
    for y_index in range(len(data)-1):
        node1 = (x_index, y_index)
        node2 = (x_index, y_index+1)
        wert = data[y_index+1][x_index]

        # my_dict[node1] = {node2:wert}
        if node1 in my_dict:
            edge_n1_n2 = my_dict[node1]
            edge_n1_n2[node2] = wert
        else:    
            edge_n1_n2 = dict()
            edge_n1_n2[node2] = wert
            my_dict[node1] = edge_n1_n2
        
        # my_dict[node2] = {node1:wert}
        if node2 in my_dict:
            edge_n2_n1 = my_dict[node2]
            edge_n2_n1[node1] = wert
        else:
            edge_n2_n1 = dict()
            edge_n2_n1[node1] = wert
            my_dict[node2] = edge_n2_n1

path_list = []
start = (0,0)
end = (len(data[0])-1,len(data)-1 )
path_list, risk = find_path(my_dict, start, end)
print(path_list)
print(risk)

