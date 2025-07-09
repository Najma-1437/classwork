class Graphs:
    # directed graph has
    def __init__(self, directed=False):
        self.directed=directed
        # Representing the graph in memory using a dictionary

        self.adj_List = dict()
        # TWO WAYS OF REPRESENTING A GRAPH IN PYTHON , ADJACENT MATRIX AND ADJACENT LIST
        # Adjacency matrix, nodes in form of a table to fill in 1 and 0
        # Adjaceny list , nodes in form of a dictionary holding key(node) and value(neighbors) for every node

    def __repr__(self):
        graph_string = ""
        for node, neighbours in self.adj_List.items():
            graph_string += f"{node} -> {neighbours}\n"
        return graph_string

    # method to add a node/vertex to the graph

    def add_node(self, node):
        # checking for duplicates so that nodes are not repeating themselves in the adjlist
        if node not in self.adj_List:
            self.adj_List[node] = set()
            # if its existing
        else:
            raise ValueError("Node already exists")
        # method to add edges

    def add_edge(self, from_node, to_node, weight=None):
        # directing the vertices to their neighbours
        # the vertice and edge is going to is the destination node  and coming from is the source node
        # checking if the node already exists in the adjlist(in the graph)
        if from_node not in self.adj_List:
            # calling the method add node that will add a node to the graph without any neighbours
            self.add_node(from_node)
        if to_node not in self.adj_List:
            self.add_node(to_node)

        if weight is None:
            self.adj_List[from_node].add(to_node)
            # if the graph is undirected , take care of two cases
            if not self.directed:
                self.adj_List[to_node].add(from_node)
        else:
            # create the connection with a weight in between the two values
            self.adj_List[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_List[to_node].add((from_node, weight))

    def bfs(self, start_node):  # using queues
        visited = set()
        queue = [start_node] # hold a node and the respective neighbours
        order = []
        # pop(dequeue), add the neighbours to the queue,pop , add neighbours, mark as visited and then when the queue is empty , you exit the method

        while queue:
            #  temporary node to allow us to traverse through the queue
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                # accessing the neighbours
                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)
        return order

    def dfs(self, start_node):  # using stack
        visited = set()
        stack = [start_node]  # hold a node and the respective neighbours
        order = []
        # pop(dequeue), add the neighbours to the queue,pop , add neighbours, mark as visited and then when the queue is empty , you exit the method

        while stack:
            #  temporary node to allow us to traverse through the queue
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # accessing the neighbours
                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def obtain_neighbours(self, node):
        return self.adj_List.get(node, set()) # returns the node and the neighbours as a set


if __name__ == "__main__":
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge("A", "B", 2)
    graph_obj.add_edge("A", "J", 6)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)

    print("GRAPH STRUCTURE:\n", graph_obj)
    print("BREADTH FIRST SEARCH:\n", graph_obj.bfs("A"))
    print("DEPTH FIRST SEARCH:\n", graph_obj.dfs("A"))


