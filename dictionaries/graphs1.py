# dictionaries can be used to represent graphs:
# "a graph is a collection of vertices (/nodes) connected by edges (which are ARROWS)"
# e.g.
# g = {
#   "a": ["b", "d"],
#   "b": ["c"]
# } ...would represent vertex "a" pointed to "b" and "d" and vertex "b" pointed to vertex "c"

# take a graph, and the names of two nodes, and determine if there is an edge from node 1 to node 2:
g = {
  "a": ["b", "d"],
  "b": ["c"]
}

def isNode(node1, node2, graph):
    try:
        if node2 in graph[node1] or node1 in graph[node2]:
            return True
        else:
            return False
    except:
        return False

# print(isNode("b","a", g))