"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else: 
            return set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = deque()
        visited = set()
        queue.append(starting_vertex)

        while len(queue) > 0:
            curNode = queue.popleft()
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.get_neighbors(curNode):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)

        while len(stack) > 0:
            curNode = stack.pop()
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.get_neighbors(curNode):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)

        while len(stack) > 0:
            curNode = stack.pop()
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.get_neighbors(curNode):
                    self.dft_recursive(neighbor)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()

        queue.append([starting_vertex])
        visited = set()

        while len(queue) > 0:
            curPath = queue.popleft()
            curNode = curPath[-1]

            if curNode == destination_vertex:
                return curPath
            if curNode not in visited:
                visited.add(curNode)
                for neighbor in self.get_neighbors(curNode):
                    newPath = list(curPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()

        stack.append([starting_vertex])
        visited = set()

        while len(stack) > 0:
            curPath = stack.pop()
            curNode = curPath[-1]

            if curNode == destination_vertex:
                return curPath
            if curNode not in visited:
                visited.add(curNode)
                for neighbor in self.get_neighbors(curNode):
                    newPath = list(curPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = deque()
        stack.append([starting_vertex])
        visited = set()

        while len(stack) > 0:
            curPath = stack.pop()
            curNode = curPath[-1]

            if curNode == destination_vertex:
                return curPath
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.get_neighbors(curNode):
                    newPath = list(curPath)
                    self.dfs_recursive(neighbor)
                    # newPath.append(neighbor)
                    # stack.append(newPath)

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
