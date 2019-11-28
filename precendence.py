# https://www.geeksforgeeks.org/python-program-for-topological-sorting/
# HOW WE MODIFIED IT ACIKLANACAK
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self, id):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if i in self.graph[id]:
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        stack.insert(0, id)
        return stack


def nameconverter(namespace, output_list):
    #for i in output_list:
    #    print(i)
    new_list = [namespace[i] for i in output_list]
    return new_list

def main():
    print("=== Ex. 1 ===")
    g = Graph(6)
    namespace = ["CAIVehicle", "CPuppet", "CPipeUser", "CAIPlayer", "CAIActor", "CAIObject"]
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 5)

    print("For 'CAIVehicle' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("CAIVehicle"))))
    print("For 'CAIPlayer' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("CAIPlayer"))))
    print("=== End of Ex. 1 ===\n")

    print("=== Ex. 2 ===")
    namespace = ["fstream", "ifstream", "iostream", "ofstream", "istream", "ostream", "ios"]
    g = Graph(7)
    g.addEdge(0, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)

    print("For 'ifstream' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("ifstream"))))
    print("For 'fstream' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("fstream"))))
    print("For 'ofstream' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("ofstream"))))
    print("=== End of Ex. 2 ===\n")

    print("=== Ex. 3 ===")
    namespace = ["Consultant Manager", "Director", "Permanent Manager", "Consultant", "Manager", "Temporary Employee", "Permanent Employee", "Employee"]
    g = Graph(8)
    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 6)
    g.addEdge(3, 5)
    g.addEdge(4, 7)
    g.addEdge(6, 7)
    g.addEdge(5, 7)

    print("For 'Consultant Manager' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("Consultant Manager"))))
    print("For 'Director' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("Director"))))
    print("For 'Permanent Manager' -> ", nameconverter(namespace, g.topologicalSort(namespace.index("Permanent Manager"))))
    print("=== End of Ex. 3 ===\n")


if __name__ == '__main__':
    main()
