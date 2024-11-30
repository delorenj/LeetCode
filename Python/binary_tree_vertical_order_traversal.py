"""
Problem: Binary Tree Vertical Order Traversal
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column)
If two nodes are in the same row and column, the order should be from left to right.
Here are the requirements and constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
"""
from typing import List

class Node:
    def __init__(self, val:int, index:int) -> None:
        self.val = val
        self.index = index
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)
    
    def __repr__(self) -> str:
        return self.__str__()

def tree(root: List[int]) -> Node:
    if len(root) == 0: return None
    
    i=0
    nodes = [Node(root[i], 0)]
    for i in range(len(root)):
        print(i, nodes)
        current = nodes[i]
        li = i*2+1
        ri = i*2+2
        if li < len(root):
            n = Node(root[li], current.index-1)
            current.left = n
            nodes.append(n)
        if ri < len(root):
            n = Node(root[ri], current.index+1)
            current.right = n
            nodes.append(n)
    
    return nodes[0]

def printtree(root: Node, columns) -> None
    columns = {root[index]: [node]}
    result = []
    for key in sorted(columns):
        result.append(columns[key])

    print(result)

root = tree([3,9,20,None,None,15,7])
printtree(root)
