'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

Example
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

Notice
You need return the node with the same label as the input node.


'''

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here 
        if node is None:
            return None
        # step 1: find nodes by BFS
        nodes = self.find_nodes_BFS(node)
        # step 2: copy nodes
        mapping = self.copy_nodes(nodes)
        # step 3: copy edges
        self.copy_edges(nodes, mapping)
        
        return mapping[node]
        
    def find_nodes_BFS(self, root):
        visited = set([root])
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue 
                visited.add(neighbor)
                queue.append(neighbor)
                
        return list(visited)
            
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping
        
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
    
