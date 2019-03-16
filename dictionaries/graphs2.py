# extending the function from graphs1, we shall now determine if there is a path between two nodes:

from graphs1 import isNode

g = {
    "a": ["b", "d"],
    "b": ["c"],
    "c": ["f"],
    "d": ["e"],
    "e": ["b","f"],
    "f": []
}

def isPath(node1,node2,graph):
    if(isNode(node1,node2,graph) == True):
        return True
    else:
        seen_node = []
        for node in graph[node1]:
            seen_node.append(node)
            if(isNode(node,node2,graph) == True):
                return True
            print(seen_node)
        for item in seen_node:
            routes=[]
            if(graph[item] not in seen_node):
                routes.append(graph[item])
        
                
    return False
 
print(isPath("a","f", g))