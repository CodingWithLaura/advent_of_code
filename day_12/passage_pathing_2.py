def graph_list_to_graph_dict(graph_list, graph_dict):
    for connection in graph_list:
        if connection[0] in graph_dict:
            graph_dict[connection[0]].append(connection[1])
        else:
            graph_dict[connection[0]] = [connection[1]]
        if connection[1] in graph_dict:
            graph_dict[connection[1]].append(connection[0])
        else:
            graph_dict[connection[1]] = [connection[0]]    

def allready_twice_in_path(path):
    for item in path:
        if item.islower():
            twice = 0
            for otheritem in path:
                if(item == otheritem):
                    twice +=1
            if(twice > 1):
                return True
    return False
            
def filter_nodes(node_liste, delete_node_liste):
    already_twice = allready_twice_in_path(delete_node_liste)
    result_list = node_liste.copy()
    potential_twice_visited_caves = {'start','end'}
    for item in node_liste:
        for to_delete in delete_node_liste:
            if (item == to_delete) and (to_delete.islower()):
                if (item in potential_twice_visited_caves) or (already_twice):
                    if(item in result_list): # don't delte the item twice
                        result_list.remove(item)
                else:
                    potential_twice_visited_caves.add(item)
    return result_list

def remove_node(node,liste):
    liste.remove(node)
    
def find_paths(start_node,end_node, graph_dict):
    paths = []
    next_nodes = []
    next_nodes.append(graph_dict[start_node].copy())
    path = [start_node]
    abbruch = True
    while (abbruch):
    # for nodes in next_nodes:
        if(next_nodes == []):
            break
        nodes = next_nodes[len(next_nodes)-1].copy()
        if(nodes == []):
            to_delete = path.pop()
            next_nodes.pop()
            if(next_nodes != []):
                remove_node(to_delete, next_nodes[len(next_nodes)-1])
        else:    
            node = nodes.pop()
            path.append(node)
            if(node == 'end'):
                paths.append(path.copy())
                remove_node('end',next_nodes[len(next_nodes)-1])
                path.pop()
            else:
                #backtrack
                potential_nodes = graph_dict[node].copy()
                filtered_next_nodes = filter_nodes(potential_nodes, path)
                next_nodes.append(filtered_next_nodes)
                #abruch bedingung hier abruch = False
    return paths

graph_list = []

f = open("real_numbers.txt", "r")
lines = f.readlines()
for line in lines:
    graph_list.append(line.rstrip("\n").split("-"))
    
print(graph_list)
graph_dict = {}
graph_list_to_graph_dict(graph_list, graph_dict)
print(graph_dict)

all_paths = []
all_paths = find_paths('start','end', graph_dict)
print(all_paths)
print(len(all_paths))
