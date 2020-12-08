'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:



The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?

Clarification
Learn more about representation of graphs

Notice
You can assume that there is at least one topological order in the graph.
'''


"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        node_to_degrees = self.get_degrees(graph)
        result = []
        queue = collections.deque([node for node in graph if node_to_degrees[node] == 0])
        while queue:
            head = queue.popleft()
            result.append(head)
            for neighbor in head.neighbors:
                node_to_degrees[neighbor] -= 1
                if node_to_degrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return result
            
    def get_degrees(self, graph):
        node_to_degrees = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_to_degrees[neighbor] += 1
        return node_to_degrees
