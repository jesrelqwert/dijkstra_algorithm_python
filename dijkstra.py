class Graph:
    def __init__(self, nodes_in_graph = []):
        self.nodes_in_graph = nodes_in_graph

    def add_node(self, node):
        self.nodes_in_graph.append(node)

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)



class Node:
    def __init__(self, nodename, connections):
        self.nodename = nodename
        self.connections = connections

        self.cost_table = {nodename: {'cost':0, 'previous':None}}

        for name, cost in self.connections.items():
            self.cost_table[name] = {'cost': cost, 'previous': self.nodename}


    def __repr__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections:{self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'
    
    def __str__(self):
        cost_table_header = '\tNode\tCost\tPrevious\n'
        cost_table_str = ''.join([f'\t{node}\t{vals["cost"]}\t{vals["previous"]}\n' for node, vals in self.cost_table.items()])

        return f'nodename: {self.nodename}\nconnections:{self.connections}\ncost_table:\n {cost_table_header}{cost_table_str}'
    
    def build_cost_table(self, graph):
        """
        dijkstra

        El costo del nodo a si mismo = 0
        La tabla de costo se llena con todos los nodos en el grafo
        La distancia a todos los nodos = 10**9 (e.g. infinito)

        Repetir:
            visita el nodo sin visitar con la distancia más corta conocida desde el nodo de comienzo
                for current node, examine its unvisited neighbors
                for current node, calc the distance of each neighbor from this start node
                if the calc distance of a node is less than the current distance in the cost table, upodate the shortest distance in the cost table
                update de previous node for each update distance
                add the current node to the list of visited nodes and remove it ftom the list of unvisited nodes
        untill all nodes are visited
        """
        visited = [self.nodename]

        # Llenar la tabla de costo con los nodos restantes del grafo
        # Se establece la distancia para todos los otros nodos = 10**9
        for node in graph.nodes_in_graph:
            if node.nodename not in self.cost_table:
                self.cost_table[node.nodename] = {'cost':10**9, 'previous':None}





if __name__ == '__main__':
    # Se definen nodos
    A = Node('A', {'B':5, 'C':7, 'D':2})
    B = Node('B', {'A':5, 'E':4})
    C = Node('C', {'A':7, 'D':3, 'F':5})
    D = Node('D', {'A':2, 'C':3, 'E':4, 'G':6})
    E = Node('E', {'B':4, 'D':4, 'G':2})
    F = Node('F', {'C':5, 'G':7, 'H':6})
    G = Node('G', {'E':2, 'D':6, 'F':7, 'H':3})
    H = Node('H', {'G':3, 'F':6})

    #print(A)

    graph = Graph()
    graph.add_nodes([A, B, C, D, E, F, G, H])

    A.build_cost_table(graph)    
    print(A)

    #print(graph.nodes_in_graph)
