"""
Title: 2458. Height of Binary Tree After Subtree Removal Queries

Difficulty: Hard

Topics: Array, Tree, Depth-First Search (DFS), Breadth-First Search (BFS), Binary Tree

Description: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/?envType=daily-question&envId=2024-10-26

"""
from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

from typing import Optional

"""
APPROACH: Two-Pass Depth First Search (Preorder Traversal -> Reverse Preorder Traversal)

INTUITION: Looking at the constraints on the number of nodes and the number of queries (2 <= n <= 10^5 and 1 <= q <= min(n, 10^4) respectively), we cannot
use a brute force method where we run a complete depth-first search (DFS) for each query and store the maximum height found each time. Ideally we only do 
one or two passes of the whole tree while storing the information we need to provide the answer. Examining a binary tree, it seems that the height of a 
binary tree after a subtree rooted at some node is removed is just the max height of the binary tree before reaching that node... sort of. Assuming we do 
a preorder traversal (parent -> left child -> right child), this logic works if the node is in the right subtree, but fails if the node is in the left 
subtree. For example:
    Say we want to remove the subtree rooted at node 4...
          1
       3     4
     2     6   5
                 7
    The above tree would return 2 as the height of the tree when node 4 is removed because we are able to first get the height from the left subtree,
    but in the following tree,
             1
        4         3
      6   5     2   
            7
    we would return 0 as the height of the tree when node 4 is removed because the proposed logic doesn't let us explore the right subtree before deciding
    the height of the tree when node 4 is removed.
We can fix this logical error by doing a second pass on the tree in reverse preorder (parent -> right child -> left child) and taking the maximum between
the height found in the first pass and the height found in the second pass. This means that we can do two passes on the whole tree storing the max height
of the tree before reaching each node, and then return the relevant heights based on the nodes in queries.
    
    ALGORITHM:
        - For the main treeQueries(root, queries) function:
            - Initialize an array of 0s with length equal to 1 + the maximum possible number of nodes. We'll call this array heights
            - Initialize an array with a single 0 value to store the max tree height found during a pass. We'll call this array max_height
            - Run a preorder traversal, storing the max between the current max height and heights[current_node_value] (i.e. run dfs(), with the reverse parameter
            being False)
            - Reinitialize max_height to [0] before doing the next pass
            - Run a reverse preorder traversal, storing the max between the current max height and heights[current_node_value] (i.e. run dfs(), with the reverse parameter
            being True)
            - For every query in queries, return heights[query] to get the height of the tree when the subtree at node query is removed
        - For the recursive dfs(node, height, heights, max_height, reverse) function:
            - Check that the current node (called node) exists
                - If it does not, end the recursive call with a return
                - If it does, keep going
            - Update the number in heights at the current node's value (heights[node.val]) with the maximum between the current max height value (max_height[0]) 
            and the existing height value at heights[node.val]
            - Update the max_height[0] with the max between the current value of max_height[0] and the height of the current node (called height)
            - If the reverse parameter is True, then we recursively call dfs() on the current node's right subtree and then call dfs() on the recursive call's left
            subtree (reverse preorder traversal)
            - If the reverse parameter is False, then we recursively call dfs() on the current node's left subtree and then call dfs() on the recursive call's right
            subtree (preorder traversal)
COMPLEXITY:
    TIME: O(n + q), where n is the number of nodes in the tree and q is the number of queries
        - There are two major contributors to the space complexity: the two complete passes through the tree and the iteration through queries to get the
        result:
            - There are n nodes in the tree and we visit each one twice which takes O(2*n) time. 
            - We have to iterate through q queries to create the result array which takes O(q) time.
        - Therefore the overall time complexity for this solution O(2*n + q) which simplifies to O(n)
    SPACE: O(n)(!), where n is the number of nodes in the tree
        - There are two major contributors to the space complexity: the heights array and the recursive call stack
            - The heights array will always have a length of 100001, which means the space allocated for it is independent of the input size and thus
            is O(1)
            - The recursive call stack has a worst case height of n (occurs when the tree is extremely unbalanced, and has depth n), making the call
            stack take O(n) space
        - Therefore the overall space complexity is O(1 + n) which simplifies to O(n).
        - NOTE(!) If the tree is well balanced, its depth can be approximated by log(n) which would make the recursive call stack take O(log(n)) space, 
        resulting in an overall space complexity of O(log(n))
                

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # Beat anywhere from 19.21% to 54.61% on Runtime
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = [0]*100001

        max_height = [0]; self.dfs(root, 0, heights, max_height, False)
        max_height = [0]; self.dfs(root, 0, heights, max_height, True)
        
        return [heights[query] for query in queries]
    
    def dfs(self, node, height, heights, max_height, reverse):
        if not node: return
        heights[node.val] = max(heights[node.val], max_height[0])
        max_height[0] = max(max_height[0], height)
        if reverse: # reverse preorder traversal
            self.dfs(node.right, height + 1, heights, max_height, reverse)
            self.dfs(node.left, height + 1, heights, max_height, reverse)
        else: # normal preorder traversal
            self.dfs(node.left, height + 1, heights, max_height, reverse)
            self.dfs(node.right, height + 1, heights, max_height, reverse)
"""
APPROACH: Single Pass Depth-First Search

INTUITION: TODO #11

    ALGORITHM:

COMPLEXITY: TODO #12
    TIME:
    SPACE:

"""  

# TODO #13

if __name__=="__main__":
    print(Solution())
