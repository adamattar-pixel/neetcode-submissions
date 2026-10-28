"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        hashmap = defaultdict(list)
        stack = [node]
        while stack:
            q = stack.pop()
            if q.val in hashmap: continue
            hashmap[q.val] = Node(q.val, q.neighbors)
            stack += q.neighbors

        for el in hashmap:
            hashmap[el].neighbors = [hashmap[n.val] for n in hashmap[el].neighbors]
    
        return hashmap[1]