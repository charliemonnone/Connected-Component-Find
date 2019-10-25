def read_file():
    test_file_1 = open("HW3test4.txt","r")
    lines = []
    for line in test_file_1.readlines():
        lines.append(line.rstrip())
    test_file_1.close()
    return lines

def build_adjacency_list(vertex_count, edges):
    adj = [[] for i in range(vertex_count+1)]
    for edge in edges:
        verticies = edge.split()
        v1 = int(verticies[0])
        v2 = int(verticies[1])
        adj[v1].append(v2)
        adj[v2].append(v1)
    return adj

def connected_component_find(visited, adj):
    component_count = 0
    for i in range(1,len(visited)):
        if not visited[i]:
            component = []
            component_count += 1
            print("Component " + str(component_count) + ": ")
            dfs(i, visited, adj, component)
            print(component)
            print(" ")
              
def dfs(vertex, visited, adj, component):
    visited[vertex] = True
    component.append(vertex)
    for v in adj[vertex]:
        if not visited[v]:
            dfs(v,visited, adj, component)

data_list = read_file()
edge_count = int(data_list[0])
vertex_count = int(data_list[1])
edge_list = data_list[2:]
adjacency_list = build_adjacency_list(vertex_count, edge_list)
visited = []
for i in range(vertex_count+1):
    visited.append(False)
connected_component_find(visited, adjacency_list)
