"""
Given a reference of a node in a connected undirected graph
Return a deep copy (clone) of the graph
Each node in the graph contains a value (int) and a list(List[Node]) of its neighbors
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

For simplicity, each nodes value is the same as the nodes index (1-indexed),
for example the first node with val == 1, the second node with val == 2
The graph is represented in the test case using an adjacency list
An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1, you must
return the copy of the given node as a reference to the cloned graph.
"""

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None
    
    #create hash map to store the copy of each node
    copies = {}
    
    #perform DFS traversal on the original graph
    self.cloneGraphHelper(node, copies)
    
    #return the copy of the first node
    return copies[node]
    
  def cloneGraphHelper(self, node, copies):
    #create a copy of the node
    copy = Node(node.val)
    #add the copy to the hash map
    copies[node] = copy
    #copy the neighbors
    for neighbor in node.neighbors:
      if neighbor not in copies:
        #if the neighbor hasnt been copied, create its copy
        self.cloneGraphHelper(neighbor, copies)
      #add the copy of the neighbor to the neighbor list of the copy
      #of the node
      copy.neighbors.append(copies[neighbor])
