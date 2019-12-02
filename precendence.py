# https://www.geeksforgeeks.org/python-program-for-topological-sorting/
# HOW WE MODIFIED IT ACIKLANACAK
from collections import defaultdict


class Graph:
    def __init__(self, vertices, namespace):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.namespace = namespace

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
        print("Step for ", self.nameconverter([stack[0]]), ": ", self.nameconverter(stack))
        input()

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self, id):
        print("\nPress any key to continue the step.")
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

    def nameconverter(self, output_list):
        new_list = [self.namespace[i] for i in output_list]
        return new_list


def main():
    print("=== Ex. 1 ===")
    g = Graph(6, ["CAIVehicle", "CPuppet", "CPipeUser", "CAIPlayer", "CAIActor", "CAIObject"])
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 5)

    print("Result for EXAMPLE 1.1: 'CAIVehicle' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("CAIVehicle"))))
    print("Result for EXAMPLE 1.2: 'CAIPlayer' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("CAIPlayer"))))
    print("=== End of Ex. 1 ===\n")

    print("=== Ex. 2 ===")
    g = Graph(7, ["fstream", "ifstream", "iostream", "ofstream", "istream", "ostream", "ios"])
    g.addEdge(0, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)

    print("Result for EXAMPLE 2.1: 'ifstream' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("ifstream"))))
    print("Result for EXAMPLE 2.2: 'fstream' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("fstream"))))
    print("Result for EXAMPLE 2.3: 'ofstream' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("ofstream"))))
    print("=== End of Ex. 2 ===\n")

    print("=== Ex. 3 ===")
    g = Graph(8, ["Consultant Manager", "Director", "Permanent Manager", "Consultant", "Manager", "Temporary Employee", "Permanent Employee", "Employee"])
    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 6)
    g.addEdge(3, 5)
    g.addEdge(4, 7)
    g.addEdge(6, 7)
    g.addEdge(5, 7)

    print("Result for EXAMPLE 3.1: 'Consultant Manager' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("Consultant Manager"))))
    print("Result for EXAMPLE 3.2: 'Director' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("Director"))))
    print("Result for EXAMPLE 3.3: 'Permanent Manager' -> ", g.nameconverter(g.topologicalSort(g.namespace.index("Permanent Manager"))))
    print("=== End of Ex. 3 ===\n")


if __name__ == '__main__':
    main()
